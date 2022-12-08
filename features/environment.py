from appium import webdriver
from app.application import Application
import os

basedir = os.path.abspath(os.path.join(__file__, "../.."))


def before_scenario(context, scenario):
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities={'platformName': 'Android',
                                                            'platformVersion': '11.0',
                                                            'deviceName': 'Pixel',
                                                            'automationName': 'UiAutomator2',
                                                            'app': basedir + u'/app/binaries/EXAMPLE.apk',
                                                            'appPackage': '',
                                                            'autoAcceptAlerts': 'true',  # to accept all alerts
                                                            'autoGrantPermissions': 'true'
                                                            })

    context.driver.implicitly_wait(30)

    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
