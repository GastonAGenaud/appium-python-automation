from selenium.common import NoSuchElementException
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class EntregarPedidoPage(Page):
    restar_btn = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="-"])[1]')
    entregar_btn = (MobileBy.ACCESSIBILITY_ID, 'Confirmar')
    precio_total_factura = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 872.818"]')
    precio_rebajado = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 57.652"]')
    confirmar_btn = (MobileBy.ACCESSIBILITY_ID, 'Confirmar')
    entrega_completada_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="¡Entrega impecable!"]')
    cerrar_cuadro_btn = (MobileBy.XPATH, '//android.widget.FrameLayout['
                                         '@resource-id="android:id/content"]/android.widget.FrameLayout/android.view'
                                         '.ViewGroup['
                                         '2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
    modificar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Modificar"]')
    modifica_tu_ruta_texto = (MobileBy.XPATH, '//android.widget.TextView[@text="Modifica tu ruta"]')

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

    def click_confirmar_boton(self):
        self.click_on_element(self.confirmar_btn)

    def click_modificar_btn(self):
        try:
            self.click_on_element(self.modificar_btn)
            self.click_on_element(self.modificar_btn)
            self.find_element(self.modifica_tu_ruta_texto).is_displayed()
            #self.implicit_wait_visible(self.modifica_tu_ruta_texto)
        except NoSuchElementException:
            self.click_on_element(self.modificar_btn)
            self.click_on_element(self.modificar_btn)

    def valido_entrega_completada(self):
        self.implicit_wait_visible(self.entrega_completada_txt)
        valido_entrega = self.find_element(self.entrega_completada_txt).is_displayed()
        return valido_entrega

    def click_cerrar_boton(self):
        self.click_on_element(self.cerrar_cuadro_btn)
