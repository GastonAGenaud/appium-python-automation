from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class ModificarRecorridoPage(Page):
    comenzar_ruta_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Comenzar ruta"]')
    el_deseo_spa_local = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="address"]')
    boton_desplegable_mas = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Más productos"]')
    boton_desplegable_menos = (MobileBy.XPATH, '//android.widget.TextView[@text="Menos productos"]')
    boton_desplegable_ruta = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Ruta sugerida"]')
    mas_productos_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Más productos"]')
    menos_productos_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Menos productos"]')
    ruta_sugerida_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Ruta sugerida"]')
    modificar_manualmente_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Modificar manualmente"]')
    comenzar_ruta_msg = (MobileBy.XPATH, '//android.widget.TextView[@text="Ruta comenzada"]')
    modifica_tu_ruta_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="Modifica tu ruta"]')
    presiona_prolongadamente_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="Presiona prolongadamente al cliente que deseas reordenar y luego desplázalo hacia su nueva posición."]')
    entendido_boton = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Entendido"]')
    no_volver_a_mostrar_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="No volver a mostrar"]')

    def valido_comenzar_ruta_btn(self):
        self.implicit_wait_visible(self.comenzar_ruta_btn)
        valido_comenzar_ruta = self.find_element(self.comenzar_ruta_btn).is_displayed()
        return valido_comenzar_ruta

    def valid_value(self, caracteristica, valor):
        self.implicit_wait_visible(self.comenzar_ruta_btn)
        value = self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="{valor}"]').is_displayed()
        return value

    def valido_el_deseo_spa_local(self):
        self.implicit_wait_visible(self.el_deseo_spa_local)
        nombre_local = self.find_element(self.el_deseo_spa_local).is_displayed()
        return nombre_local

    def click_comenzar_ruta_btn(self):
        self.click_on_element(self.comenzar_ruta_btn)
        self.click_on_element(self.comenzar_ruta_btn)

    def click_dedsplegador_btn(self):
        self.click_on_element(self.boton_desplegable_ruta)
        self.click_on_element(self.boton_desplegable_ruta)
        self.click_on_element(self.boton_desplegable_menos)

    def valido_mas_productos_opcion(self):
        self.implicit_wait_visible(self.mas_productos_texto)
        valido_mas_productos = self.find_element(self.mas_productos_texto).is_displayed()
        return valido_mas_productos

    def valido_menos_productos_opcion(self):
        self.implicit_wait_visible(self.menos_productos_texto)
        valido_menos_productos = self.find_element(self.menos_productos_texto).is_displayed()
        return valido_menos_productos

    def valido_rutas_sugerida_opcion(self):
        self.implicit_wait_visible(self.ruta_sugerida_texto)
        valido_rutas_sugerida = self.find_element(self.ruta_sugerida_texto).is_displayed()
        return valido_rutas_sugerida

    def valido_comenzar_ruta_msg(self):
        self.implicit_wait_visible(self.comenzar_ruta_msg)
        valido_comenzar_ruta = self.find_element(self.comenzar_ruta_msg).is_displayed()
        return valido_comenzar_ruta

    def valido_texto_modifica_tu_ruta(self):
        self.implicit_wait_visible(self.modifica_tu_ruta_txt)
        valido_texto = self.find_element(self.modifica_tu_ruta_txt).is_displayed()
        return valido_texto

    def valido_texto_preiona_prolongadamente(self):
        self.implicit_wait_visible(self.presiona_prolongadamente_txt)
        valido_texto = self.find_element(self.presiona_prolongadamente_txt).is_displayed()
        return valido_texto

    def valido_texto_entendido(self):
        self.implicit_wait_visible(self.entendido_boton)
        valido_texto = self.find_element(self.entendido_boton).is_displayed()
        return valido_texto

    def valido_texto_no_volver_a_mostrar(self):
        self.implicit_wait_visible(self.no_volver_a_mostrar_txt)
        valido_texto = self.find_element(self.no_volver_a_mostrar_txt).is_displayed()
        return valido_texto
