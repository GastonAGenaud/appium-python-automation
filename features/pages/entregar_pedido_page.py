from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class EntregarPedidoPage(Page):
    restar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="-"]')
    entregar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Entregar"]')
    precio_total_factura = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 38.000"]')
    precio_rebajado = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 2.000"]')
    confirmar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Confirmar"]')
    entrega_completada_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="¡Entrega impecable!"]')

    def rebajo_el_pedido(self):
        self.click_on_element(self.restar_btn)

    def valido_precio_total_factura(self):
        self.implicit_wait_visible(self.precio_total_factura)
        precio_total = self.find_element(self.precio_total_factura).is_displayed()
        return precio_total

    def valido_precio_rebajado(self):
        self.implicit_wait_visible(self.precio_rebajado)
        valor_precio_rebajado = self.find_element(self.precio_rebajado).is_displayed()
        return valor_precio_rebajado

    def click_confirmar_btn(self):
        self.click_on_element(self.confirmar_btn)

    def valido_entrega_completada(self):
        self.click_on_element(self.entrega_completada_txt)
        valido_entrega = self.find_element(self.entrega_completada_txt).is_displayed()
        return valido_entrega
