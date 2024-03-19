from appium.webdriver.common.mobileby import MobileBy
from features.pages.base_page import Page


class AnulacionPage(Page):
    def validar_pantalla_anulacion(self):
        return True

    def visualizar_pantalla_anulacion(self):
        return True

    def validar_presencia_motivos(self, motivos):
        return True

    def validar_presencia_boton_enviar(self):
        return True

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
        return True

    def visualizar_pantalla_retomar_pedidos(self):
        return True

    def validar_ruta_pedido(self, ruta):
        return True

    def validar_presencia_boton_retomar_pedido(self):
        return True

    def clic_retomar_pedido(self):
        return True

    def verificar_redireccion_detalles(self):
        return True

    def verificar_pedido_retomar(self):
        return True

    def validar_presencia_boton_ver_detalle(self):
        return True

    def clic_ver_detalle(self):
        return True

    def verificar_redireccion(self):
        return True
