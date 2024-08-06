import re
import time
from telnetlib import EC
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class RebajarPedidoPage(Page):
    retornado_sobre_stock = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc=" Retornada - Sobre stock, '
                                             'Factura N° 404145531, Productos, 10, Cheque, '
                                             '$ 0"]/android.view.ViewGroup[1]')

    def valido_precio_final_rebajado(self):
        valor_total = self.find_element(MobileBy.XPATH, '//android.widget.TextView[@resource-id="total-price"]')
        precio_producto_total = valor_total.text
        solo_numeros_total = re.sub(r'\D', '', precio_producto_total)
        precio_producto_total = int(solo_numeros_total)
        # Aquí puedes hacer algo con el precio calculado, como imprimirlo
        print("Precio total del producto rebajado:", precio_producto_total)
        return precio_producto_total

    def motivo_anulacion_pantalla_lista(self, motivos):
        for motivo in motivos:
            motivo_element = (MobileBy.XPATH, f"//*[@text='{motivo}']")
            if not self.scroll_down_until_element(motivo_element):
                print(f"Motivo no encontrado: {motivo}")  # Logging para motivos no encontrados
                return False
        return True

    def scroll_down_until_element(self, locator,
                                  max_scrolls=20):  # Aumentar el número máximo de intentos de desplazamiento
        scroll_attempts = 0
        while scroll_attempts < max_scrolls:
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return True
            except NoSuchElementException:
                self.scroll_down()
                scroll_attempts += 1
                print(f"Intento de scroll: {scroll_attempts}")  # Logging para intentos de scroll
                time.sleep(1.5)  # Aumentar el tiempo de espera entre cada intento de scroll
        return False

    def scroll_down(self):
        # Aumenta la duración para un scroll más lento y más profundo
        self.driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=300, duration=1500)

    def implicit_wait_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"El elemento con el locator {locator} no se visualizó dentro del tiempo especificado."
        )
