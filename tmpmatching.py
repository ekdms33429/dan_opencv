#https://m.blog.naver.com/samsjang/220587092117
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

    img = cv2.imread('screencap.png') #원본 이미지
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #원본 이미지
    template = cv2.imread('img/kakaobtn.png', cv2.IMREAD_GRAYSCALE) # 템플릿 이미지, grayscale 이미지 사용
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)#템플릿 매칭 함수 matchTemplate(원본 이미지, 템플릿 이미지, 템플릿 매칭 플래그) / 이미지는 8비트의 단일 채널 이미지 사용
        #매칭 수식 TM_SQDIFF / TM_SQDIFF_NORMED / TM_CCORR / TM_CCORR_NORMED / TM_CCOEFF / TM_CCOEFF_NORMED
        #(W, H) 원본 이미지 크기 / (w, h) 템플릿 이미지 크기
        # 결과값은 32비트 단일 채널, (W-w+1, H-h+1) 배열의 크기
        # 템플릿 이미지로 비교하기 때문에 검출된 이미지 또한 템플릿 이미지와 동일한 크기
    loc = np.where(res >= thr) # (array_row, array_column) row = y, column = x

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    TouchAction(driver).tap(x=pt[0] + w / 2, y=pt[1] + h / 2).perform()

    #창 띄워서 영역 확인-red rectangle
    img_scale = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)  # fx, fx = 이미지 가로/세로 사이즈의 배수
    cv2.imshow("Matching Result", img_scale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    tmpMatching(0.95)