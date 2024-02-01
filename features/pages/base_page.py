from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element = self.driver.find_element(by=locator[0], value=locator[1])
        element.click()

    def type_phone(self):
        # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_1
        element = self.driver
        # Type in the keyboard
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

    def scroll_to_element(self, locator):
        """
        Scrolls the mobile view until the element specified by the locator is in view.
        """
        try:
            element = self.find_element(locator)

            if self.driver.capabilities['platformName'].lower() == 'android':
                # Para Android, utilizando UIAutomator2
                self.driver.execute_script("mobile: scroll", {"strategy": "accessibility id",
                                                              "selector": element.accessibility_id,
                                                              "action": "visible"})
            else:
                # Para iOS, utilizando Mobile: scroll
                self.driver.execute_script("mobile: scroll", {"element": element.id,
                                                              "toVisible": True})
        except TimeoutException:
            print("Element not found to scroll to")
