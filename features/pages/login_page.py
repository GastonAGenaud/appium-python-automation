from selenium.common import NoSuchElementException
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(Page):
    # title_lbl = (MobileBy.ID, 'com.skill2lead.appiumdemo:id/imageView')
    # phone_txt = (MobileBy.CLASS_NAME, a'android.widget.EditText')
    login_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='Login']")
    password_txt = (MobileBy.XPATH, "//android.widget.EditText[@text='Password']")
    loginbutton = (MobileBy.ID, 'com.skill2lead.appiumdemo:id/Login')
    enterEmail = (MobileBy.ID, 'com.skill2lead.appiumdemo:id/Et4')
    enterPassword = (MobileBy.ID, 'com.skill2lead.appiumdemo:id/Et5')
    clickloginButton = (MobileBy.ID, 'com.skill2lead.appiumdemo:id/Btn3')
    wrongCredentials = "Wrong Credentials"  # text
    pageTitle = (MobileBy.CLASS_NAME, 'android.widget.TextView')
    enterText = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    submitButton = (MobileBy.ID, 'com.skill2lead.appiumdemo:id/Btn_admin_sub')
    successLoginPopUp = (MobileBy.XPATH, '//android.widget.FrameLayout['
                                         '@resource-id="android:id/content"]/android.widget.LinearLayout')
    continueButton = MobileBy.CLASS_NAME, 'android.widget.Button'
    welcomeMessage = MobileBy.XPATH, '//android.widget.TextView[@text="Bienvenido, Test!"]'
    updateState1 = MobileBy.XPATH, '//android.widget.Button[@content-desc="Update State 1"]'
    updateState2 = MobileBy.XPATH, '//android.widget.Button[@content-desc="Update State 2"]'

    # def login_with_email_and_password(self):
    #     self.click_on_element(self.login_btn)
    #     self.click_on_element(self.password_txt)
    #     self.input(PASSWORD, self.password_txt)
    #     self.driver.hide_keyboard()
    #     self.click_on_element(self.login_btn)

    def login_successfully(self):
        if not self.is_logged_in():
            # self.click_on_element(self.loginbutton)
            self.input("Test", self.enterText)
            self.click_on_element(self.continueButton)
            self.scroll_to_element(self.updateState1)
            self.click_on_element(self.updateState1)
            self.scroll_to_element(self.updateState2)
            self.click_on_element(self.updateState2)
            # self.input("admin123", self.enterPassword)
            # self.click_on_element(self.clickloginButton)
            #
            # assert self.is_logged_in(), "El inicio de sesión no fue exitoso."
            #
            # self.input("Code2Lead", self.enterText)
            # self.click_on_element(self.submitButton)

    def is_logged_in(self):
        return self.is_element_present(self.welcomeMessage)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

        # TODO: Validar que se utilicen credenciales correctas (No hay botón "Reintentar")

