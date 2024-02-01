from appium import webdriver
from src.application import Application
import os

basedir = os.path.abspath(os.path.join(__file__, "../.."))


def before_scenario(context, scenario):
    try:
        context.driver = webdriver.Remote("http://127.0.0.1:4723", desired_capabilities={
            'platformName': 'android',
            'platformVersion': '14.0',
            'deviceName': 'Pixel XL API 34',
            'automationName': 'UiAutomator2',
            'app': basedir + r'/app-ruta-digital.apk',
            'appPackage': 'com.rutadigital',
        })

        context.driver.implicitly_wait(30)
        context.app = Application(context.driver)
    except Exception as e:
        print(f"Error in before_scenario: {e}")
        raise e
