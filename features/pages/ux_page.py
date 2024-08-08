import os
import re
import calendar
import time
import unicodedata
import numpy as np
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from features.pages.base_page import Page


class UXPage(Page):
    el_deseo_spa_pedido = (
        MobileBy.XPATH, "//android.widget.TextView[@resource-id='title-location' and @text='El Deseo SPA']")
    comenzar_ruta_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Comenzar ruta"]')

    def scroll_down_until_element(self, locator, max_attempts=10):
        attempts = 0
        move_end_executed = False

        while attempts < max_attempts:
            try:
                element = self.driver.find_element(*locator)
                return element
            except NoSuchElementException:
                print(f"Intento {attempts + 1} de {max_attempts} fallido. Desplazando hacia abajo.")
                if not move_end_executed:
                    self.driver.press_keycode(AndroidKey.MOVE_END)
                    move_end_executed = True

                # Realiza un desplazamiento hacia abajo más largo
                self.driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=500, duration=500)
                attempts += 1

        raise NoSuchElementException(f"Elemento no encontrado después de {max_attempts} intentos: {locator}")

    def click_el_deseo_spa_btn(self):
        element = self.driver.find_element(*self.el_deseo_spa_pedido)
        element.click()

    def valid_value(self, caracteristica, valor):
        self.implicit_wait_visible(self.comenzar_ruta_btn)
        element = self.scroll_down_until_element(self.el_deseo_spa_pedido)
        element.is_displayed()
        value = self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="{valor}"]').is_displayed()
        return value

    def valido_tamano_ingresar_btn(self, boton):
        boton = self.driver.find_element(MobileBy.XPATH, f'{boton}')
        tamano = boton.size
        ancho = tamano['width']
        alto = tamano['height']

        return ancho >= 48 and alto >= 48

    def limpiar_nombre_archivo(self, texto):
        # Normalizar el texto para remover acentos y caracteres especiales
        texto_normalizado = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
        # Remover caracteres no alfanuméricos
        nombre_archivo = re.sub(r'\W+', '', texto_normalizado)
        return nombre_archivo

    def capturar_captura_elemento(self, xpath):
        elemento = self.driver.find_element(MobileBy.XPATH, xpath)
        ruta_directorio = "features/screenshots"
        if not os.path.exists(ruta_directorio):
            os.makedirs(ruta_directorio)

        nombre_archivo = self.limpiar_nombre_archivo(xpath)
        ts = calendar.timegm(time.gmtime())

        ruta_captura = os.path.join(ruta_directorio, f"captura_{nombre_archivo}_{ts}.png")
        elemento.screenshot(ruta_captura)
        return ruta_captura

