import unittest

from PIL import Image
from appium import webdriver
from helper import android_driver, appium_command
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import cv2
import base64
import numpy as np
from matplotlib import pyplot as plt

class MyTestCase(unittest.TestCase):
    def test_templatematching(self):
        '''
        driver = android_driver()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@text, '로그인')]")))
        driver.save_screenshot('screencap.png')
        '''
        src = cv2.imread("screencap.png", cv2.IMREAD_GRAYSCALE) #원본 이미지
        templit = cv2.imread("img/kakaobtn.png", cv2.IMREAD_GRAYSCALE) # 템플릿 이미지, grayscale 이미지 사용
        dst = cv2.imread("screencap.png") #결과이미지

        result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED) #템플릿 매칭 함수 matchTemplate(원본 이미지, 템플릿 이미지, 템플릿 매칭 플래그) / 이미지는 8비트의 단일 채널 이미지 사용
        #매칭 수식 TM_SQDIFF / TM_SQDIFF_NORMED / TM_CCORR / TM_CCORR_NORMED / TM_CCOEFF / TM_CCOEFF_NORMED
        #(W, H) 원본 이미지 크기 / (w, h) 템플릿 이미지 크기
        # 결과값은 32비트 단일 채널, (W-w+1, H-h+1) 배열의 크기
        # 템플릿 이미지로 비교하기 때문에 검출된 이미지 또한 템플릿 이미지와 동일한 크기

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result) #최소, 최대 위치 함수 = 최소 포인터, 최대 포인터, 최소 지점, 최대 지점
        x, y = minLoc # 검출 위치의 좌측 상단 모서리 좌표 = minLoc or maxLoc
        h, w = templit.shape

        dst = cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 1)
        dst_scale = cv2.resize(dst, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA) #fx, fx = 이미지 가로/세로 사이즈의 배수
        #보간법 interpolation method: INTER_CUBIC 바이큐빅 보간법, 사이즈 늘릴 때(느림) / INTER_LINEAR 쌍선형 보간법, 사이즈 늘릴 때(default) / INTER_AREA 영역 보간법, 사이즈 줄일 때
        #cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
        cv2.imshow("dst", dst_scale)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


"""    
    def test_imagelocator(self):
        driver = android_driver()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@text, '로그인')]")))
        encoded_image = base64.b64encode(open("img/kakaobtn.png", "rb").read())
        print(encoded_image)
        #encode = base64.b64encode(img)
        #driver.find_element_by_image(encoded_image).click()
        #driver.update_settings({"getMatchedImageResult": True})
        #el = driver.find_element_by_image(encoded_image)
        find_result = driver.find_image_occurrence("screencap.png", "img/kakaobtn.png")
        print(find_result)


        #el.get_attribute('visual')  # returns base64 encoded string"""


def tmpMatching(thr):
    img = cv2.imread('screencap.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('img/kakaobtn.png', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= thr) # (array_row, array_column) row = y, column = x

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    cv2.imshow('res', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #unittest.main()
    tmpMatching(0.8)


