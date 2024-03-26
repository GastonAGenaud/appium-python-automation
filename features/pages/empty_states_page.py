from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from features.pages.base_page import Page


class EmptyStatesPage(Page):
    EMAIL_TEXTBOX = (MobileBy.ID, "")
    PASSWORD_TEXTBOX = (MobileBy.ID, "")
    BOTON_INGRESAR_ID = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Ingresar']")
    VISITADOS_BUTTON = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Visitados']")
    SCREEN_TEXT = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Visitados']")
    TEXTO_VISITAS = (MobileBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget"
                                     ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view"
                                     ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                     "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/com"
                                     ".horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[33]")

    def ingreso_el_correo_electronico(self, correo):
        correo_element = self.find_element(self.EMAIL_TEXTBOX)
        correo_element.clear()
        correo_element.send_keys(correo)

    def ingreso_la_contrasena(self, contrasena):
        contrasena_element = self.find_element(self.PASSWORD_TEXTBOX)
        contrasena_element.clear()
        contrasena_element.send_keys(contrasena)

    def seleccionar_opcion_visitados(self):
        try:
            # Esperar hasta que el botón 'Visitados' sea clickeable
            boton_visitados = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.VISITADOS_BUTTON)
            )

            # Obtener las coordenadas del botón 'Visitados'
            location = boton_visitados.location
            size = boton_visitados.size
            x = location['x'] + size['width'] // 2
            y = location['y'] + size['height'] // 2

            # Simular un toque en las coordenadas del botón 'Visitados'
            TouchAction(self.driver).tap(None, x, y).perform()

        except TimeoutException:
            print("Tiempo de espera agotado. El botón 'Visitados' no es clickeable.")

        except TimeoutException:
            print("Tiempo de espera agotado. El botón 'Visitados' no es clickeable.")


def valido_el_texto_visitados(self, texto):
    try:
        valido_texto = self.find_element(self.TEXTO_VISITAS).text
        return texto in valido_texto
    except NoSuchElementException:
        return False


def valido_la_pantalla(self, pantalla):
    try:
        pantalla_actual = self.find_element(self.SCREEN_TEXT).text
        return pantalla_actual == pantalla
    except NoSuchElementException:
        return False
