from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class CuadrarPage(Page):
    textoRutaMayo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-route"]')
    texto25Clientes = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-quantity"]')

    def validar_texto_ruta_mayo(self):
        self.implicit_wait_visible(self.textoRutaMayo)
        return self.find_element(self.textoRutaMayo).is_displayed()

    def validar_texto_25_clientes(self):
        self.implicit_wait_visible(self.texto25Clientes)
        return self.find_element(self.texto25Clientes).is_displayed()
