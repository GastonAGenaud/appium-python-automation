from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy
import time


class AnularPedidoPage(Page):
    # Localizadores de elementos
    retornar_pedido = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Retornar pedido"]')
    sobre_stock = (MobileBy.ACCESSIBILITY_ID, 'Sobre stock, 10')
    confirmar_btn = (MobileBy.ACCESSIBILITY_ID, "Confirmar")
    cliente_retornado_mensaje = (MobileBy.ACCESSIBILITY_ID, ", Cliente retornado")
    motivo_anulacion_pantalla = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout')
    anulados_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Retornados"]/android.view.ViewGroup')
    retomar_pedido_btn = (MobileBy.ACCESSIBILITY_ID, "Retomar pedido")
    detalles_pedido_pantalla = (MobileBy.XPATH, '//android.widget.TextView[@text=" Retornada - Sobre stock"]')
    redireccion = (MobileBy.ID, "redireccion")
    deseo_spa_retornados_locator = (MobileBy.ACCESSIBILITY_ID, "EL DESEO SPA, Sobre stock, AVDA ANDRES BELLO 2447, "
                                                               "Abierto, Cierra a las 23:59, Productos , 16, "
                                                               "Efectivo, $866.455")
    click_retornadosBtn = (
        MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Retornados"]/android.view.ViewGroup')
    textoPorqueRetornar = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="HeaderCustom"]')

    # Métodos para interactuar con la página y validar elementos

    def valido_texto_porque_retornar(self):
        self.implicit_wait_visible(self.textoPorqueRetornar)
        return self.find_element(self.textoPorqueRetornar).is_displayed()

    def valido_numero_de_factura(self, numero_factura):
        numero_de_factura = (MobileBy.XPATH, f"//android.widget.TextView[@text='Factura N° {numero_factura}']")
        self.implicit_wait_visible(numero_de_factura)
        return self.find_element(numero_de_factura).is_displayed()

    def valido_pantalla_motivo_anulacion(self):
        self.implicit_wait_visible(self.motivo_anulacion_pantalla)
        return self.find_element(self.motivo_anulacion_pantalla).is_displayed()

    def valido_motivos_anulacion(self, motivos):
        for motivo in motivos:
            motivo_element = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout')
            self.implicit_wait_visible(motivo_element)
            if not self.find_element(motivo_element).is_displayed():
                return False
        return True

    def valido_boton_enviar_motivo(self):
        self.implicit_wait_visible(self.confirmar_btn)
        return self.find_element(self.confirmar_btn).is_displayed()

    def click_enviar_motivo_btn(self):
        self.click_on_element(self.confirmar_btn)

    def seleccionar_nombre(self, nombre):
        nombre_element = (MobileBy.XPATH, f"//android.widget.TextView[@text='{nombre}']")
        self.implicit_wait_visible(nombre_element)
        self.find_element(nombre_element).click()

    def click_anulados_btn(self):
        self.click_on_element(self.anulados_btn)

    def valido_ruta_presente(self, id_ruta):
        ruta_element = (MobileBy.XPATH, f"//android.widget.TextView[@text='{id_ruta}']")
        self.implicit_wait_visible(ruta_element)
        return self.find_element(ruta_element).is_displayed()

    def valido_texto_sobre_stock(self):
        sobre_stock_element = (MobileBy.XPATH, "//android.widget.TextView[@text='Sobre stock']")
        self.implicit_wait_visible(sobre_stock_element)
        return self.find_element(sobre_stock_element).is_displayed()

    def valido_boton_comenzar_ruta(self):
        self.implicit_wait_visible(self.confirmar_btn)
        return self.find_element(self.confirmar_btn).is_displayed()

    def valido_pantalla_retomar_pedidos(self):
        self.implicit_wait_visible(self.retomar_pedido_btn)
        return self.find_element(self.retomar_pedido_btn).is_displayed()

    def valido_ruta_pedido(self, ruta):
        ruta_element = (MobileBy.XPATH, f"//android.widget.TextView[@text='{ruta}']")
        self.implicit_wait_visible(ruta_element)
        return self.find_element(ruta_element).is_displayed()

    def valido_boton_retomar_pedido(self):
        self.implicit_wait_visible(self.retomar_pedido_btn)
        return self.find_element(self.retomar_pedido_btn).is_displayed()

    def click_retomar_pedido_btn(self):
        self.click_on_element(self.retomar_pedido_btn)

    def valido_redireccion_detalles(self):
        self.implicit_wait_visible(self.detalles_pedido_pantalla)
        return self.find_element(self.detalles_pedido_pantalla).is_displayed()

    def valido_pedido_retomar(self):
        self.implicit_wait_visible(self.detalles_pedido_pantalla)
        return self.find_element(self.detalles_pedido_pantalla).is_displayed()

    def valido_boton_ver_detalle(self):
        self.implicit_wait_visible(self.confirmar_btn)
        return self.find_element(self.confirmar_btn).is_displayed()

    def click_ver_detalle_btn(self):
        self.click_on_element(self.confirmar_btn)

    def valido_redireccion(self):
        self.implicit_wait_visible(self.redireccion)
        return self.find_element(self.redireccion).is_displayed()

    def click_confirmar_btn(self):
        self.implicit_wait_visible(self.confirmar_btn)
        self.click_on_element(self.confirmar_btn)

    def valido_mensaje_validacion_retornado(self):
        mensaje_retornado_element = (
            MobileBy.XPATH, "//android.widget.TextView[@text='Mensaje de validacion de retornado']")
        self.implicit_wait_visible(mensaje_retornado_element)
        return self.find_element(mensaje_retornado_element).is_displayed()

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
            elemento = wait.until(EC.visibility_of_element_located(self.deseo_spa_retornados_locator))
            return elemento.is_displayed()
        except (NoSuchElementException, TimeoutException) as e:
            # Manejar el caso donde el elemento no se encuentra
            print(f"Elemento 'El Deseo SPA Retornados' no encontrado: {e}")
            return False
        except Exception as e:
            # Manejar cualquier otra excepción
            print(f"Ocurrió un error: {e}")
            return False

    def selecciono_boton_retornado(self):
        # Intentar hacer clic en el botón "Retornados"
        wait = WebDriverWait(self.driver, 20)  # Aumentado a 20 segundos
        try:
            boton_retornados = wait.until(EC.visibility_of_element_located(self.click_retornadosBtn))
            print("Botón 'Retornados' visible, intentando hacer clic...")
            boton_retornados.click()
            time.sleep(2)  # Esperar 2 segundos entre los clics
            boton_retornados.click()
            print("Clic en el botón 'Retornados' realizado con éxito.")
        except TimeoutException:
            print("Error: El botón 'Retornados' no está visible después de 20 segundos.")
        except NoSuchElementException:
            print("Error: No se pudo encontrar el botón 'Retornados'.")
        except Exception as e:
            print(f"Error al hacer clic en el botón 'Retornados': {e}")
