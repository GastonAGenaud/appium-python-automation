import re

from selenium.common import NoSuchElementException

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
                return False
        return True

    def scroll_down_until_element(self, locator, max_scrolls=10):
        scroll_attempts = 0
        while scroll_attempts < max_scrolls:
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return True
            except NoSuchElementException:
                self.scroll_down()
                scroll_attempts += 1
        return False

    def scroll_down(self):
        # Implementa la lógica para desplazarse hacia abajo en la pantalla
        # Esto puede variar según tu implementación específica de Appium
        self.driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=500,
                          duration=500)  # Duración más corta para un scroll más rápido
