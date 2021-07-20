import unittest
from appium import webdriver
from helper import android_driver, appium_command

class MyTestCase(unittest.TestCase):
    def test_opencv(self):
        desired_cap = {
            "deviceName": "Galaxy Note10+",
            "platformName": "Android",
            "app": "C:\\Users\\KIWIPLUS\\Desktop\\apk\\kiwiplay-v1.1.1(111)-stage-debug.apk",
            "automationName": "Uiautomator2",
            "udid": "R3CM70H0BAV"
        }
        self.webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.webdriver.implicitly_wait(10)


if __name__ == '__main__':
    unittest.main()
