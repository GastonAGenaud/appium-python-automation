import re
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
            motivo_element = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout')
            self.implicit_wait_visible(motivo_element)
            if not self.find_element(motivo_element).is_displayed():
                return False
        return True
