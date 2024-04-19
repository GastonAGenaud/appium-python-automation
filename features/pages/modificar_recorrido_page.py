from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class ModificarRecorridoPage(Page):
    comenzar_ruta_btn = (MobileBy.XPATH, '//android.widget.TextView[@text="Comenzar ruta"]')
    nro_factura = (MobileBy.XPATH, '//android.widget.TextView[@text="Factura N° 388717884"]')

    def valido_comenzar_ruta_btn(self):
        self.implicit_wait_visible(self.comenzar_ruta_btn)
        valido_comenzar_ruta = self.find_element(self.comenzar_ruta_btn).is_displayed()
        return valido_comenzar_ruta

    def valid_value(self, caracteristica, valor):
        self.implicit_wait_visible(self.comenzar_ruta_btn)
        value = self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="{valor}"]').is_displayed()
        return value

    def valido_nro_factura(self):
        self.implicit_wait_visible(self.nro_factura)
        nro_de_factura = self.find_element(self.nro_factura).is_displayed()
        return nro_de_factura

    def click_comenzar_ruta_btn(self):
        self.click_on_element(self.comenzar_ruta_btn)