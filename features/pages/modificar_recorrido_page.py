from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class ModificarRecorridoPage(Page):
    iniciar_vuelta_btn = (MobileBy.XPATH,
                          '//android.view.ViewGroup[@content-desc="Iniciar vuelta"]')
    el_deseo_spa_local = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="address"]')
    boton_desplegable_mas = (MobileBy.XPATH, '(//android.widget.TextView[@text="Más cajas primero"])[1]')
    boton_desplegable_menos = (MobileBy.XPATH, '//android.widget.TextView[@text="Menos cajas primero"]')
    boton_desplegable_ruta = (MobileBy.XPATH, '//android.widget.TextView[@text="Ruta"]')
    boton_desplegable_personalizado = (MobileBy.XPATH, '//android.widget.TextView[@text="Personalizado"]')
    ruta_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Ruta"]')
    mas_cajas_texto = (
    MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Más cajas primero"]')
    menos_cajas_texto = (
    MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and @text="Menos cajas primero"]')
    personalizado_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="menu-item-title" and '
                                           '@text="Personalizado"]')
    comenzar_ruta_msg = (MobileBy.XPATH, '//android.widget.TextView[@text="0 de 25 clientes completados"]')
    modifica_tu_ruta_txt = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="modal-alert-title"]')
    presiona_prolongadamente_txt = (MobileBy.ID, 'modal-alert-subtitle')
    entendido_boton = (MobileBy.ACCESSIBILITY_ID, 'Entendido')
    no_volver_a_mostrar_txt = (MobileBy.XPATH, '//android.widget.CheckBox[@resource-id="Test Checkbox"]')
    boton_desplegable = (MobileBy.XPATH,
                         '//android.view.ViewGroup[@content-desc="GASTRONOMICA LUSA SPA, ANTONIO BELLET 345, Abierto, '
                         'Cierra a las 20:00, Productos , 35, 3 métodos de pago, $1.778.687"]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView')
    mover_hacia_arriba_boton = (MobileBy.ACCESSIBILITY_ID, 'Mover hacia arriba')
    mover_a_lo_mas_abajo_boton = (MobileBy.ACCESSIBILITY_ID, 'Mover a lo más abajo')
    mover_hacia_arriba_mensaje = (MobileBy.ACCESSIBILITY_ID, ', Cliente ubicado arriba de la lista')
    mover_hacia_abajo_mensaje = (MobileBy.ACCESSIBILITY_ID, ', Cliente ubicado al final de la lista')
    cerrar_pedido_boton = (MobileBy.XPATH, '//com.horcrux.svg.SvgView[@resource-id="closeIcon"]')
    vueltaComenzadaValidar = (MobileBy.XPATH, '//android.widget.TextView[@text="0 de 25 clientes completados"]')

    def valido_comenzar_vuelta_boton(self):
        self.implicit_wait_visible(self.iniciar_vuelta_btn)
        valido_mensaje_vuelta_comenzada = self.find_element(self.vueltaComenzadaValidar).is_displayed()
        return valido_mensaje_vuelta_comenzada

    def valido_personalizado_opcion(self):
        self.implicit_wait_visible(self.personalizado_texto)
        valido_personalizado_texto = self.find_element(self.personalizado_texto).is_displayed()
        return valido_personalizado_texto

    def valido_comenzar_ruta_btn(self):
        self.implicit_wait_visible(self.comenzar_ruta_btn)
        valido_comenzar_ruta = self.find_element(self.comenzar_ruta_btn).is_displayed()
        return valido_comenzar_ruta

    def valido_el_deseo_spa_local(self):
        self.implicit_wait_visible(self.el_deseo_spa_local)
        nombre_local = self.find_element(self.el_deseo_spa_local).is_displayed()
        return nombre_local

    def iniciar_vuelta_button(self):
        self.implicit_wait_visible(self.iniciar_vuelta_btn)
        button_iniciar_vuelta = self.find_element(self.iniciar_vuelta_btn).is_displayed()
        return button_iniciar_vuelta

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_iniciar_vuelta_btn(self):
        while True:
            self.click_on_element(self.iniciar_vuelta_btn)
            try:
                WebDriverWait(self.driver, 5).until_not(
                    EC.presence_of_element_located(self.iniciar_vuelta_btn)
                )
                print("El botón ha desaparecido.")
                break
            except TimeoutException:
                print("El botón aún está presente. Intentando nuevamente...")

    def click_desplegador_btn(self):
        # Espera hasta que el botón sea visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.boton_desplegable_mas)
        )
        # Hace clic en el botón
        self.click_on_element(self.boton_desplegable_mas)

    def valido_mas_cajas_opcion(self):
        self.implicit_wait_visible(self.mas_cajas_texto)
        valido_mas_cajas = self.find_element(self.mas_cajas_texto).is_displayed()
        return valido_mas_cajas

    def valido_ruta_opcion(self):
        self.implicit_wait_visible(self.ruta_texto)
        valido_ruta_texto = self.find_element(self.ruta_texto).is_displayed()
        return valido_ruta_texto

    def valido_menos_cajas_opcion(self):
        self.implicit_wait_visible(self.menos_cajas_texto)
        valido_menos_cajas = self.find_element(self.menos_cajas_texto).is_displayed()
        return valido_menos_cajas

    def click_cerrar_pedido_boton(self):
        self.click_on_element(self.cerrar_pedido_boton)

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
