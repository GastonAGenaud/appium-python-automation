from appium import webdriver
from src.application import Application
import os

basedir = os.path.abspath(os.path.join(__file__, "../.."))


def before_scenario(context, scenario):
    context.driver = webdriver.Remote("http://127.0.0.1:4723",
                                      desired_capabilities={'platformName': 'Android',
                                                            'platformVersion': '13.0',
                                                            'deviceName': 'Pixel 7 Pro API 33',
                                                            'automationName': 'UiAutomator2',
                                                            'src': basedir + u'/src/binaries/app-ruta-digital.apk',
                                                            'appPackage': 'com.rutadigital',
                                                            'appActivity': 'com.rutadigital.MainActivity'
                                                            })

    context.driver.implicitly_wait(30)

    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
