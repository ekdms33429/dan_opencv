import unittest
from appium import webdriver
from helper import android_driver, appium_command
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import cv2
import numpy as np
from matplotlib import pyplot as plt

class MyTestCase(unittest.TestCase):
    def test_image(self):
        '''
        driver = android_driver()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@text, '로그인')]")))
        driver.save_screenshot('screencap.png')
        '''
        src = cv2.imread("screencap.png", cv2.IMREAD_GRAYSCALE)
        templit = cv2.imread("img/kakaobtn.png", cv2.IMREAD_GRAYSCALE)
        dst = cv2.imread("screencap.png")

        result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        x, y = minLoc
        h, w = templit.shape

        dst = cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 1)
        cv2.imshow("dst", dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        '''
        target_img = cv2.imread("screencap.png")
        find_img = cv2.imread("img/kakaobtn.png")
        find_height, find_width, find_channel = find_img.shape[::]

        # Template matching
        result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
        img_match = cv2.minMaxLoc(result)
        self.x = self.y = None
        self.x = img_match[3][0]
        self.y = img_match[3][1]



        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # Calculate location
        pointUpLeft = max_loc
        pointLowRight = (max_loc[0] + find_width, max_loc[1] + find_height)
        pointCentre = (max_loc[0] + (find_width / 2), max_loc[1] + (find_height / 2))

        #return cv2.rectangle(target_img, pointUpLeft, pointLowRight)
        '''

if __name__ == '__main__':
    unittest.main()


