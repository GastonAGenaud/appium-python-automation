from selenium.common import NoSuchElementException
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(Page):
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
    continueButton = (MobileBy.CLASS_NAME, 'android.widget.Button')
    welcomeMessage = (MobileBy.XPATH, '//android.widget.TextView[@text="Bienvenido, Test!"]')
    updateState1 = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Update State 1"]')
    updateState2 = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Update State 2"]')
    detailsBtn = (MobileBy.NAME, 'Details')
    pedidosBtn = (MobileBy.NAME, 'Pedidos')
    cameraBtn = (MobileBy.NAME, 'Camera')

    def login_successfully(self):
        if not self.is_logged_in():
            self.input("Test", self.enterText)
            self.click_on_element(self.continueButton)

    def selectingOptions(self):
        print("Starting option selection...")
        if not self.is_logged_in():
            print("Not logged in.")
            self.input("Test", self.enterText)
            print("Text entered successfully.")
            self.click_on_element(self.continueButton)
            print("ContinueButton element clicked.")
            self.click_on_element(self.detailsBtn)
            print("DetailsBtn element clicked.")
            self.click_on_element(self.ordersBtn)
            print("OrdersBtn element clicked.")
            self.click_on_element(self.cameraBtn)
            print("CameraBtn element clicked.")

    def is_logged_in(self):
        return self.is_element_present(self.welcomeMessage)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

        # TODO: Validar que se utilicen credenciales correctas (No hay botón "Reintentar")
