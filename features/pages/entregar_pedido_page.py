from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class EntregarPedidoPage(Page):

    def hacer_clic_ingresar(self):
        return True

    def elegir_ruta(self, nombreRuta):
        return True

    def seleccionar_comenzar_ruta(self):
        return True

    def visualizar_pantalla_rebajados(self, numeroFactura):
        return True

    def visualizar_pantalla_entregados(self, numeroFactura):
        return True

    def validar_producto_presente(self, nombreProducto):
        return True

    def validar_total_factura(self, totalFactura):
        return True

    def validar_total_rebajado(self, totalRebajado):
        return True

    def validar_presencia_boton_confirmar(self):
        return True

    def seleccionar_boton_confirmar(self):
        return True

    def verificar_redireccion_confirmacion(self):
        return True
