from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class LaunchPage(Page):
    title_lbl = (MobileBy.CLASS_NAME, 'android.widget.ImageView')
    phone_txt = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    login_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='Login']")

    def login_with_existing_account(self):
        self.implicit_wait_visible(self.title_lbl)
        self.click_on_element(self.phone_txt)
        self.type_phone()
        self.implicit_wait_visible(self.title_lbl)
