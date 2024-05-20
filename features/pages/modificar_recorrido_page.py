from appium.webdriver.common.touch_action import TouchAction
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
    modifica_tu_ruta_txt = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="modal-alert-title"]')
    presiona_prolongadamente_txt = (MobileBy.ID, 'modal-alert-subtitle')
    entendido_boton = (MobileBy.ACCESSIBILITY_ID, 'Entendido')
    no_volver_a_mostrar_txt = (MobileBy.XPATH, '//android.widget.CheckBox[@resource-id="Test Checkbox"]')
    el_deseo_spa = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-location" and @text="EL DESEO SPA"]')
    boton_desplegable = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="COMERCIAL Y GASTRONOMICA ..., AVENIDA ISIDORA GOYENECHEA 2971, Abierto, Cierra a las 23:59"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView')
    mover_hacia_arriba_boton = (MobileBy.ACCESSIBILITY_ID, 'Mover hacia arriba')
    mover_a_lo_mas_abajo_boton = (MobileBy.ACCESSIBILITY_ID, 'Mover a lo más abajo')

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

    def click_desplegador_btn(self):
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
        #valido_texto = self.driver.find_element_by_id("00000000-0000-004a-ffff-ffff000001e2").is_displayed()
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

    def click_entendido_boton(self):
        self.click_on_element(self.entendido_boton)

    def click_desplegar_boton(self):
        self.click_on_element(self.boton_desplegable)

    def click_mover_hacia_arriba_boton(self):
        self.click_on_element(self.mover_hacia_arriba_boton)

    def click_mover_a_lo_mas_abajo_boton(self):
        self.click_on_element(self.mover_a_lo_mas_abajo_boton)

    #def drag_text_box_down(self):
        #text_box = self.driver.find_element_by_xpath(self.'//android.widget.TextView[@resource-id="title-location" and @text="EL DESEO SPA"]')
        #actions = TouchAction(self.driver)
        #actions.long_press(element = text_box).move_to(x=0, y=100).release().perform()

