from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class CuadrarPage(Page):
    textoRutaMayo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-route"]')
    texto25Clientes = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-quantity"]')
    rutaComenzar = (MobileBy.ACCESSIBILITY_ID, ', Ruta comenzada')
    textoRutaEntregada = (MobileBy.XPATH, '//android.widget.TextView[@text="Entregada"]')
    confirmar_btn = (MobileBy.ACCESSIBILITY_ID, 'Confirmar')
    no_hay_productos_rebajados_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="HeaderCustom"]')

    def validar_texto_ruta_mayo(self):
        self.implicit_wait_visible(self.textoRutaMayo)
        return self.find_element(self.textoRutaMayo).is_displayed()

    def validar_texto_25_clientes(self):
        self.implicit_wait_visible(self.texto25Clientes)
        return self.find_element(self.texto25Clientes).is_displayed()

    def validar_mensaje_comenzar(self):
        self.implicit_wait_visible(self.rutaComenzar)
        return self.find_element(self.rutaComenzar).is_displayed()

    def validar_texto_entregada(self):
        self.implicit_wait_visible(self.textoRutaEntregada)
        texto_entregado = self.find_element(self.textoRutaEntregada).is_displayed()
        return texto_entregado

    def validar_texto_no_hay_producto(self):
        self.implicit_wait_visible(self.no_hay_productos_rebajados_texto)
        texto_no_hay_producto = self.find_element(self.no_hay_productos_rebajados_texto).is_displayed()
        return texto_no_hay_producto
