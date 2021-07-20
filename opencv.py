import unittest
from appium import webdriver
from helper import android_driver, appium_command

class MyTestCase(unittest.TestCase):
    def test_opencv(self):
        driver = android_driver()
        print("test")


if __name__ == '__main__':
    unittest.main()
