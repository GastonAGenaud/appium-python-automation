from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class ModificarRecorridoPage(Page):
    comenzar_ruta_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Comenzar ruta"]')
    el_deseo_spa_local = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="address"]')
    boton_desplegable_mas = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Más productos"]')
    boton_desplegable_menos = (MobileBy.XPATH, '//android.widget.TextView[@text="Menos productos"]')
    boton_desplegable_ruta = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Más productos"]')
    mas_productos_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Más productos"]')
    menos_productos_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Menos productos"]')
    ruta_sugerida_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Ruta sugerida"]')
    modificar_manualmente_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Modificar manualmente"]')
    comenzar_ruta_msg = (MobileBy.XPATH, '//android.widget.TextView[@text="0 de 25 clientes completados"]')
    modifica_tu_ruta_txt = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="modal-alert-title"]')
    presiona_prolongadamente_txt = (MobileBy.ID, 'modal-alert-subtitle')
    entendido_boton = (MobileBy.ACCESSIBILITY_ID, 'Entendido')
    no_volver_a_mostrar_txt = (MobileBy.XPATH, '//android.widget.CheckBox[@resource-id="Test Checkbox"]')
    el_deseo_spa = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-location" and @text="EL DESEO SPA"]')
    boton_desplegable = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="GASTRONOMICA LUSA SPA, ANTONIO BELLET 345, Abierto, Cierra a las 20:00, Productos , 35, Pago mixto, $1.778.687"]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView')
    mover_hacia_arriba_boton = (MobileBy.ACCESSIBILITY_ID, 'Mover hacia arriba')
    mover_a_lo_mas_abajo_boton = (MobileBy.ACCESSIBILITY_ID, 'Mover a lo más abajo')
    mover_hacia_arriba_mensaje = (MobileBy.ACCESSIBILITY_ID, ', Cliente ubicado arriba de la lista')
    mover_hacia_abajo_mensaje = (MobileBy.ACCESSIBILITY_ID, ', Cliente ubicado al final de la lista')
    cerrar_pedido_boton = (MobileBy.XPATH, '//com.horcrux.svg.SvgView[@resource-id="closeIcon"]')

    def valido_comenzar_ruta_btn(self):
        self.implicit_wait_visible(self.comenzar_ruta_btn)
        valido_comenzar_ruta = self.find_element(self.comenzar_ruta_btn).is_displayed()
        return valido_comenzar_ruta

    def valido_el_deseo_spa_local(self):
        self.implicit_wait_visible(self.el_deseo_spa_local)
        nombre_local = self.find_element(self.el_deseo_spa_local).is_displayed()
        return nombre_local

    def click_comenzar_ruta_btn(self):
        max_attempts = 4  # Número máximo de intentos
        attempts = 0

        while attempts < max_attempts:
            self.click_on_element(self.comenzar_ruta_btn)
            try:
                WebDriverWait(self.driver, 2).until_not(
                    EC.presence_of_element_located(self.comenzar_ruta_btn)
                )
                print("El botón ha desaparecido.")
                break
            except TimeoutException:
                print("El botón aún está presente. Intentando nuevamente...")
                attempts += 1
                if attempts == max_attempts:
                    print("Número máximo de intentos alcanzado. El botón aún está presente.")

    def click_desplegador_btn(self):
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            self.click_on_element(self.boton_desplegable_ruta)
            try:
                WebDriverWait(self.driver, 2).until_not(
                    EC.presence_of_element_located(self.boton_desplegable_ruta)
                )
                print("El botón ha desaparecido.")
                break
            except TimeoutException:
                print("El botón aún está presente. Intentando nuevamente...")
                attempts += 1
                if attempts == max_attempts:
                    print("Número máximo de intentos alcanzado. El botón aún está presente.")
        self.click_on_element(self.boton_desplegable_menos)

    def valido_mas_productos_opcion(self):
        self.implicit_wait_visible(self.mas_productos_texto)
        valido_mas_productos = self.find_element(self.mas_productos_texto).is_displayed()
        return valido_mas_productos

    def valido_menos_productos_opcion(self):
        self.implicit_wait_visible(self.menos_productos_texto)
        valido_menos_productos = self.find_element(self.menos_productos_texto).is_displayed()
        return valido_menos_productos

    def click_cerrar_pedido_boton(self):
        self.click_on_element(self.cerrar_pedido_boton)

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

    def click_entendido_boton(self):
        self.click_on_element(self.entendido_boton)

    def click_desplegar_boton(self):
        self.click_on_element(self.boton_desplegable)

    def click_mover_hacia_arriba_boton(self):
        self.click_on_element(self.mover_hacia_arriba_boton)

    def click_mover_a_lo_mas_abajo_boton(self):
        self.click_on_element(self.mover_a_lo_mas_abajo_boton)

    def valido_mensaje_cliente_modificado_arriba(self):
        self.implicit_wait_visible(self.mover_hacia_arriba_mensaje)
        valido_texto = self.find_element(self.mover_hacia_arriba_mensaje).is_displayed()
        return valido_texto

    def valido_mensaje_cliente_modificado_abajo(self):
        self.implicit_wait_visible(self.mover_hacia_abajo_mensaje)
        valido_texto = self.find_element(self.mover_hacia_abajo_mensaje).is_displayed()
        return valido_texto
