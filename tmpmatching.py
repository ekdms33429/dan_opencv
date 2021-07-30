import cv2
import numpy as np
from appium.webdriver.common.touch_action import TouchAction

from helper import android_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def tmpMatching(thr):
    driver = android_driver()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@text, '로그인')]")))
    driver.save_screenshot('screencap.png')

    img = cv2.imread('screencap.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('img/kakaobtn.png', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= thr) # (array_row, array_column) row = y, column = x

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    TouchAction(driver).tap(x=pt[0] + w / 2, y=pt[1] + h / 2).perform()

    #창 띄워서 영역 확인_red rectangle
    img_scale = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)  # fx, fx = 이미지 가로/세로 사이즈의 배수
    cv2.imshow("Matching Result", img_scale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    tmpMatching(0.95)