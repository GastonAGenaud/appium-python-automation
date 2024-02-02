# VerticalScrolling.py

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException


class VerticalScrolling:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, text_scroll, direction='up'):
        driver = self.driver
        try:
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                f'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scroll{direction}()')
        except NoSuchElementException:
            raise NoSuchElementException(f'Elemento con texto "{text_scroll}" no encontrado para realizar scroll')

    def scroll_to_element(self, element):
        actions = TouchAction(self.driver)
        actions.press(element).release().perform()
