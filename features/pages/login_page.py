from features.credentials import CORREO
from features.credentials import CONTRASENA
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(Page):
    usuario_field = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[1]')
#   contrasena_field = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[2]')
#    login_btn = (MobileBy.XPATH, '//android.widget.TextView[@text="Login"]')

#    def user_input_name(self):
#        self.click_on_element(self.usuario_field)
#        self.input(USUARIO, self.usuario_field)

#    def user_input_password(self):
#        self.click_on_element(self.contrasena_field)
#        self.input(CONTRASENA, self.contrasena_field)
#        self.click_on_element(self.login_btn)
