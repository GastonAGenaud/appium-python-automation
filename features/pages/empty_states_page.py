from appium.webdriver.common.mobileby import MobileBy
from features.pages.base_page import Page


class EmptyStatesPage(Page):
    EMAIL_TEXTBOX = (MobileBy.ID, "")
    PASSWORD_TEXTBOX = (MobileBy.ID, "")
    OPTION_BUTTON = (MobileBy.ID, "")
    SCREEN_TEXT = (MobileBy.ID, "")
    SCREEN_TITLE = (MobileBy.ID, "")

    def ingreso_el_correo_electronico(self, correo):
        correo_element = self.find_element(*self.EMAIL_TEXTBOX)
        correo_element.clear()
        correo_element.send_keys(correo)

    def ingreso_la_contraseña(self, contraseña):
        contraseña_element = self.find_element(*self.PASSWORD_TEXTBOX)
        contraseña_element.clear()
        contraseña_element.send_keys(contraseña)

    def seleccionar_opcion(self, opcion):
        opcion_element = self.find_element(*self.OPTION_BUTTON)
        opcion_element.click()

    def valido_el_texto(self, texto):
        pantalla_texto = self.find_element(*self.SCREEN_TEXT).text
        return texto in pantalla_texto

    def valido_la_pantalla(self, pantalla):
        pantalla_actual = self.find_element(*self.SCREEN_TITLE).text
        return pantalla_actual == pantalla
