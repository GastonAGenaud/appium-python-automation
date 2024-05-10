from appium import webdriver
from src.application import Application
import os
import json

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def before_scenario(context, scenario):
    with open(os.path.join(basedir, 'config.json')) as config_file:
        config = json.load(config_file)

    context.driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        desired_capabilities=config['target']['capabilities']
    )

    context.driver.implicitly_wait(30)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()