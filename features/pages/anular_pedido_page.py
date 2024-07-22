from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy
import time


class AnularPedidoPage(Page):
    retornar_pedido = (MobileBy.ACCESSIBILITY_ID, 'Retornar pedido')
    confirmar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Confirmar"]')
    motivo_anulacion_pantalla = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout')
    deseo_spa_retornados_locator = (MobileBy.ACCESSIBILITY_ID, "EL DESEO SPA, Sobre stock, AVDA ANDRES BELLO 2447, "
                                                               "Abierto, Cierra a las 23:59, Productos , 16, "
                                                               "Efectivo, $866.455")
    textoPorqueRetornar = (MobileBy.XPATH, '//android.widget.TextView[@text=" Retornada - Sobre stock"]')
    validar_pantalla_retomar_detalles = (
        MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="EL DESEO SPA, Sobre stock, AVDA ANDRES BELLO 2447, Abierto, Cierra a las 23:59, Productos , 16, 2 métodos de pago, $866.455"]')

    def valido_pantalla_retomar(self):
        self.implicit_wait_visible(self.validar_pantalla_retomar_detalles)
        return self.find_element(self.validar_pantalla_retomar_detalles).is_displayed()

    def valido_texto_porque_retornar(self):
        element = self.find_element(self.textoPorqueRetornar)
        return element.is_displayed()

    def valido_pantalla_motivo_anulacion(self):
        self.implicit_wait_visible(self.motivo_anulacion_pantalla)
        return self.find_element(self.motivo_anulacion_pantalla).is_displayed()

    def seleccionar_nombre(self, nombre):
        nombre_element = (
            MobileBy.XPATH,
            f"//android.widget.TextView[@text='{nombre}']"
        )
        self.implicit_wait_visible(nombre_element)
        self.find_element(nombre_element).click()

    def valido_boton_ver_detalle(self):
        self.implicit_wait_visible(self.confirmar_btn)
        return self.find_element(self.confirmar_btn).is_displayed()

    def valido_cliente_retornado_mensaje(self):
        cliente_retornado_element = (MobileBy.ACCESSIBILITY_ID, ", Cliente retornado")
        self.implicit_wait_visible(cliente_retornado_element)
        return self.find_element(cliente_retornado_element).is_displayed()

    def selecciono_retornar_pedido(self):
        self.implicit_wait_visible(self.retornar_pedido)
        self.click_on_element(self.retornar_pedido)

    def deseo_spa_retornados(self):
        try:
            # Añadir espera explícita
            wait = WebDriverWait(self.driver, 20)  # Aumentado a 20 segundos
            elemento = wait.until(EC.visibility_of_element_located(self.validar_pantalla_retomar_detalles))
            return elemento.is_displayed()
        except (NoSuchElementException, TimeoutException) as e:
            # Manejar el caso donde el elemento no se encuentra
            print(f"Elemento 'El Deseo SPA Retornados' no encontrado: {e}")
            return False
        except Exception as e:
            # Manejar cualquier otra excepción
            print(f"Ocurrió un error: {e}")
            return False
