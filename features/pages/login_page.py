from features.credentials import NAME
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(Page):
    name_txt = (MobileBy.XPATH, "//android.widget.EditText[@text='Ingresa tu nombre']")
    continue_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='Continuar']")

    def user_input_name(self):
        self.click_on_element(self.name_txt)
        self.input(NAME, self.name_txt)
        self.click_on_element(self.continue_btn)
