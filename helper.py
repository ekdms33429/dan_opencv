
#import json
from typing import TYPE_CHECKING

#import httpretty

from appium import webdriver
# :return: A string of test URL
SERVER_URL_BASE = 'http://localhost:4723/wd/hub'

if TYPE_CHECKING:
    #from httpretty.core import HTTPrettyRequestEmpty

    from appium.webdriver.webdriver import WebDriver


def appium_command(command: str) -> str:
    """Return a command of Appium
    Returns:
        str: A string of command URL
    """
    return f'{SERVER_URL_BASE}{command}'


def android_driver() -> 'WebDriver':
    """Return a W3C driver which is generated by a mock response for Android
    Returns:
        `webdriver.webdriver.WebDriver`: An instance of WebDriver
    """
    desired_caps = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'platformVersion': '11',
        'deviceName': 'Galaxy Note10+ 5G',
        'app': 'C:\\Users\\KIWIPLUS\\Desktop\\apk\\kiwiplay-v1.1.1(111)-stage-debug.apk',
        'deviceUDID': 'R3CM70H0BAV'
    }

    driver = webdriver.Remote(SERVER_URL_BASE, desired_caps)
    driver.implicitly_wait(30)
    return driver


