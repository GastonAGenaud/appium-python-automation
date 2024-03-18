from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.common.exceptions import TimeoutException


class Page:
    driver: object

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(by=locator[0],
                                        value=locator[1])

    def click_on_element(self, locator):
        element = self.driver.find_element(by=locator[0],
                                           value=locator[1])
        element.click()

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
