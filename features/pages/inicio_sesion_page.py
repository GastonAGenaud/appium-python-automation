from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class InicioSesionPage(Page):
    correo_campo = (MobileBy.XPATH, '//android.widget.EditText[contains(@resource-id, "customTextInput")][1]')
    contrasena_campo = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[2]')
    mensaje_error_correo = (MobileBy.XPATH, '//android.widget.TextView[@text="Tienes que ingresar un usuario"]')
    mensaje_error_contrasena = (MobileBy.XPATH, '//android.widget.TextView[@text="Tienes que ingresar una contraseña"]')
    comenzar_ruta_btn = (MobileBy.ACCESSIBILITY_ID, 'Comenzar ruta')
    iniciar_sesion_btn = (MobileBy.ACCESSIBILITY_ID, 'Iniciar sesión')
    mensaje_saludo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-home"]')
    vueltas_disponibles_txt = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="subtitle-home"]')
    icono_back = (MobileBy.XPATH, '//com.horcrux.svg.SvgView[@resource-id="ChevronRightIcon"]')
    vuelta_iniciada_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="Iniciada"]')

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
            #self.driver.hide_keyboard()
            self.click_on_element(self.iniciar_sesion_btn)

    def click_iniciar_sesion_boton(self):
        # if self.driver.is_keyboard_shown():
        #self.driver.hide_keyboard()

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

    def valid_titulo_vueltas_disponible(self):
        self.implicit_wait_visible(self.vueltas_disponibles_txt)
        valido_saludo = self.find_element(self.vueltas_disponibles_txt).is_displayed()
        return valido_saludo

    def valido_pantalla_de_inicio(self):
        self.implicit_wait_visible(self.iniciar_sesion_btn)
        pantalla_inicio = self.find_element(self.iniciar_sesion_btn).is_displayed()
        return pantalla_inicio

    def valido_btn_ingresar_desactivado(self):
        self.implicit_wait_visible(self.iniciar_sesion_btn)
        ingresar_desactivado = self.find_element(self.iniciar_sesion_btn).is_enabled()
        return ingresar_desactivado

    def click_icono_back(self):
        max_attempts = 4  # Número máximo de intentos
        attempts = 0

        while attempts < max_attempts:
            self.click_on_element(self.icono_back)
            try:
                WebDriverWait(self.driver, 2).until_not(
                    EC.presence_of_element_located(self.icono_back)
                )
                print("El Icono ha desaparecido.")
                break
            except TimeoutException:
                print("El Icono aún está presente. Intentando nuevamente...")
                attempts += 1
                if attempts == max_attempts:
                    print("Número máximo de intentos alcanzado. El Icono aún está presente.")

    def valido_vuelta_iniciada_txt(self):
        self.implicit_wait_visible(self.vuelta_iniciada_txt)
        vuelta_iniciada = self.find_element(self.vuelta_iniciada_txt).is_enabled()
        return vuelta_iniciada
