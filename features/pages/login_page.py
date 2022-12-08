from features.credentials import PHONE, PASSWORD
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(Page):
    title_lbl = (MobileBy.CLASS_NAME, 'android.widget.ImageView')
    phone_txt = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    login_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='Login']")
    password_txt = (MobileBy.XPATH, "//android.widget.EditText[@text='Password']")

    def login_with_email_and_password(self):
        if not PHONE or not PASSWORD:
            raise Exception("Please add credentials to configuration file!")
        self.click_on_element(self.phone_txt)
        self.type_phone()
        self.click_on_element(self.login_btn)
        self.click_on_element(self.password_txt)
        self.input(PASSWORD, self.password_txt)
        self.driver.hide_keyboard()
        self.click_on_element(self.login_btn)

        # TODO Validate that we use correct credentials (There is no button "Retry again")
