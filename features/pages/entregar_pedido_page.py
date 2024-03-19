from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class EntregarPedidoPage(Page):
    BOTON_INGRESAR_ID = (MobileBy.ID, "boton_ingresar_id")
    RUTA_INPUT_ID = (MobileBy.ID, "ruta_input_id")
    BOTON_COMENZAR_RUTA_ID = (MobileBy.ID, "boton_comenzar_ruta_id")
    PANTALLA_REBAJADOS_ID = (MobileBy.ID, "pantalla_rebajados_id")
    PANTALLA_ENTREGADOS_ID = (MobileBy.ID, "pantalla_entregados_id")
    PRODUCTO_ESPERADO_ID = (MobileBy.ID, "producto_esperado_id")
    TOTAL_FACTURA_ID = (MobileBy.ID, "total_factura_id")
    TOTAL_REBAJADO_ID = (MobileBy.ID, "total_rebajado_id")
    BOTON_CONFIRMAR_ID = (MobileBy.ID, "boton_confirmar_id")

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
