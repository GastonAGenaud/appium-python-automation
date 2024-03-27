from features.credentials import CORREO
from features.credentials import CONTRASENA
from features.credentials import CORREO_CON_CARACTERES
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class InicioSesionPage(Page):
    correo_campo = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[1]')
    contrasena_campo = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[2]')
    ingresar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Ingresar"]')
    entendido_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Entendido"]')
    mensaje_error_correo = (MobileBy.XPATH, '//android.widget.TextView[@text="Tienes que ingresar un correo electrónico"]')
    mensaje_error_contrasena = (MobileBy.XPATH, '//android.widget.TextView[@text="Tienes que ingresar una contraseña"]')
    mensaje_error_inicio_sesion = (MobileBy.XPATH, '//android.widget.LinearLayout[@resource-id="android:id/title_template"]')
    comenzar_ruta_btn = (MobileBy.XPATH, '//android.widget.TextView[@text="Comenzar ruta"]')

    def usuario_ingresa_correo_user_tests(self):
        self.click_on_element(self.correo_campo)
        self.input(CORREO, self.correo_campo)

    def usuario_ingresa_correo_erroneo(self):
        self.click_on_element(self.correo_campo)
        self.input(CORREO_CON_CARACTERES, self.correo_campo)

    def usuario_ingresa_contrasena(self):
        self.click_on_element(self.contrasena_campo)
        self.input(CONTRASENA, self.contrasena_campo)

    def click_ingresa_btn(self):
        self.click_on_element(self.ingresar_btn)

    def valido_mensaje_error_correo(self):
        self.implicit_wait_visible(self.mensaje_error_correo)
        mensaje_error = self.find_element(self.mensaje_error_correo).is_displayed()
        return mensaje_error

    def valido_mensaje_error_contrasena(self):
        self.implicit_wait_visible(self.mensaje_error_contrasena)
        mensaje_error = self.find_element(self.mensaje_error_contrasena).is_displayed()
        return mensaje_error

    def valid_comenzar_ruta_btn(self):
        self.implicit_wait_visible(self.comenzar_ruta_btn)
        valido_comenzar_ruta = self.find_element(self.comenzar_ruta_btn).is_displayed()
        return valido_comenzar_ruta

    def valido_tamano_ingresar_btn(self):
        boton = self.driver.find_element(MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Ingresar"]')
        tamano = boton.size
        ancho = tamano['width']
        alto = tamano['height']

        if ancho >= 48 and alto >= 48:
            return True
        else:
            return False

    def valido_tamano_comenzar_ruta_btn(self):
        boton = self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Comenzar ruta"]')
        tamano = boton.size
        ancho = tamano['width']
        alto = tamano['height']

        if ancho >= 48 and alto >= 48:
            return True
        else:
            return False

    def valido_pantalla_de_inicio(self):
        self.implicit_wait_visible(self.ingresar_btn)
        pantalla_inicio = self.find_element(self.ingresar_btn).is_displayed()
        return pantalla_inicio
