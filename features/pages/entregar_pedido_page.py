from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


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
    modifica_tu_ruta_texsto = (MobileBy.ID, 'title-amount-total')

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
        max_attempts = 4  # Número máximo de intentos
        attempts = 0

        while attempts < max_attempts:
            self.click_on_element(self.modificar_btn)
            try:
                WebDriverWait(self.driver, 2).until_not(
                    EC.presence_of_element_located(self.modificar_btn)
                )
                print("El botón ha desaparecido.")
                break
            except TimeoutException:
                print("El botón aún está presente. Intentando nuevamente...")
                attempts += 1
                if attempts == max_attempts:
                    print("Número máximo de intentos alcanzado. El botón aún está presente.")

    def valido_entrega_completada(self):
        self.implicit_wait_visible(self.entrega_completada_txt)
        valido_entrega = self.find_element(self.entrega_completada_txt).is_displayed()
        return valido_entrega

    def click_cerrar_boton(self):
        self.click_on_element(self.cerrar_cuadro_btn)
