from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.common.exceptions import TimeoutException


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        return self.driver.find_elements(by=locator[0],
                                         value=locator[1])

    def find_element(self, locator):
        return self.driver.find_element(by=locator[0],
                                        value=locator[1])

    def click_on_element(self, locator):
        element = self.driver.find_element(by=locator[0],
                                           value=locator[1])
        element.click()

    def type_phone(self):
        # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_1
        element = self.driver
        # element.press_keycode(0x00000010)
        # element.press_keycode(0x00000007)
        # element.press_keycode(0x0000000a)
        # element.press_keycode(0x00000009)
        # element.press_keycode(0x0000000d)
        # element.press_keycode(0x00000008)
        # element.press_keycode(0x0000000e)
        # element.press_keycode(0x00000007)
        # element.press_keycode(0x00000007)
        # element.press_keycode(0x00000008)

        element.press_keycode(0x00000010)
        element.press_keycode(0x00000010)
        element.press_keycode(0x00000010)
        element.press_keycode(0x0000000f)
        element.press_keycode(0x0000000f)
        element.press_keycode(0x0000000f)
        element.press_keycode(0x0000000e)
        element.press_keycode(0x0000000e)
        element.press_keycode(0x0000000e)
        element.press_keycode(0x0000000e)

    def input(self, text, locator):
        password_input = self.driver.find_element(by=locator[0],
                                                  value=locator[1])
        password_input.send_keys(text)

    def implicit_wait_visible(self, locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expect.visibility_of_element_located(locator))
        except TimeoutException:
            print("Element no visible")
