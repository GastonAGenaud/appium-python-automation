from appium.webdriver.common.mobileby import MobileBy
from features.pages.base_page import Page


class AnulacionPage(Page):
    PANTALLA_ANULACION_ID = (MobileBy.ID, "")
    MOTIVOS_ID = (MobileBy.ID, "")
    BOTON_ENVIAR_ID = (MobileBy.ID, "")
    NOMBRE_ID = (MobileBy.ID, "")
    RUTA_ID = (MobileBy.ID, "")
    BOTON_COMENZAR_RUTA_ID = (MobileBy.ID, "")
    BOTON_RETOMAR_PEDIDO_ID = (MobileBy.ID, "")
    BOTON_VER_DETALLE_ID = (MobileBy.ID, "")

    def validar_pantalla_anulacion(self):
        pantalla_presente = self.find_element(self.PANTALLA_ANULACION_ID).is_displayed()
        return pantalla_presente

    def visualizar_pantalla_anulacion(self):
        return True

    def validar_presencia_motivos(self, motivos):
        motivos_presentes = self.find_element(self.MOTIVOS_ID).is_displayed()
        return motivos_presentes

    def validar_presencia_boton_enviar(self):
        boton_presente = self.find_element(self.BOTON_ENVIAR_ID).is_displayed()
        return boton_presente

    def clic_enviar_motivo(self):
        return True

    def seleccionar_nombre(self, nombre):
        return True

    def clic_anulados(self):
        return True

    def validar_ruta_presente(self, idRuta):
        return True

    def validar_texto_sobre_stock(self):
        return True

    def validar_presencia_boton_comenzar_ruta(self):
        boton_presente = self.find_element(self.BOTON_COMENZAR_RUTA_ID).is_displayed()
        return boton_presente

    def visualizar_pantalla_retomar_pedidos(self):
        return True

    def validar_ruta_pedido(self, ruta):
        return True

    def validar_presencia_boton_retomar_pedido(self):
        boton_presente = self.find_element(self.BOTON_RETOMAR_PEDIDO_ID).is_displayed()
        return boton_presente

    def clic_retomar_pedido(self):
        return True

    def verificar_redireccion_detalles(self):
        return True

    def verificar_pedido_retomar(self):
        return True

    def validar_presencia_boton_ver_detalle(self):
        boton_presente = self.find_element(self.BOTON_VER_DETALLE_ID).is_displayed()
        return boton_presente

    def clic_ver_detalle(self):
        return True

    def verificar_redireccion(self):
        return True
