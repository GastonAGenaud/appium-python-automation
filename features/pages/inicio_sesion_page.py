from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class InicioSesionPage(Page):
    correo_campo = (MobileBy.XPATH, '//android.widget.EditText[contains(@resource-id, "customTextInput")][1]')
    contrasena_campo = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[2]')
    mensaje_error_correo = (MobileBy.XPATH, '//android.widget.TextView[@text="Tienes que ingresar un usuario"]')
    mensaje_error_contrasena = (MobileBy.XPATH, '//android.widget.TextView[@text="Tienes que ingresar una contraseña"]')
    comenzar_ruta_btn = (MobileBy.ACCESSIBILITY_ID, 'Comenzar ruta')
    iniciar_sesion_btn = (MobileBy.ACCESSIBILITY_ID, 'Iniciar sesión')
    mensaje_saludo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-home"]')

    def usuario_ingresa_correo(self, correo, logged_in):
        if not logged_in:
            self.click_on_element(self.correo_campo)
            self.input(correo, self.correo_campo)

    def usuario_ingresa_correo_manual(self, correo):
        self.click_on_element(self.correo_campo)
        self.input(correo, self.correo_campo)

    def usuario_ingresa_contrasena(self, password, logged_in):
        if not logged_in:
            self.click_on_element(self.contrasena_campo)
            self.input(password, self.contrasena_campo)

    def usuario_ingresa_contrasena_manual(self, password):
        self.click_on_element(self.contrasena_campo)
        self.input(password, self.contrasena_campo)

    def click_iniciar_sesion_btn(self, logged_in):
        if not logged_in:
            # if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()
        self.click_on_element(self.iniciar_sesion_btn)

    def click_iniciar_sesion_boton(self):
        # if self.driver.is_keyboard_shown():
        self.driver.hide_keyboard()

        self.click_on_element(self.iniciar_sesion_btn)

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

    def valid_mensaje_saludo(self):
        self.implicit_wait_visible(self.mensaje_saludo)
        valido_saludo = self.find_element(self.mensaje_saludo).is_displayed()
        return valido_saludo

    def valido_pantalla_de_inicio(self):
        self.implicit_wait_visible(self.iniciar_sesion_btn)
        pantalla_inicio = self.find_element(self.iniciar_sesion_btn).is_displayed()
        return pantalla_inicio

    def valido_btn_ingresar_desactivado(self):
        self.implicit_wait_visible(self.iniciar_sesion_btn)
        ingresar_desactivado = self.find_element(self.iniciar_sesion_btn).is_enabled()
        return ingresar_desactivado
