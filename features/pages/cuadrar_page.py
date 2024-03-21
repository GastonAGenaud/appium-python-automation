from appium.webdriver.common.mobileby import MobileBy
from features.pages.base_page import Page


class CuadrarPage(Page):
    PRODUCTO_ESPERADO_ID = (MobileBy.ID, "")
    TOTAL_ESPERADO_ID = (MobileBy.ID, "")
    TRANSFERENCIA_ESPERADA_ID = (MobileBy.ID, "")
    EFECTIVO_ESPERADO_ID = (MobileBy.ID, "")
    CHEQUE_ESPERADO_ID = (MobileBy.ID, "")
    CREDITO_ESPERADO_ID = (MobileBy.ID, "")
    REBAJADO_ESPERADO_ID = (MobileBy.ID, "")
    BOTON_CERRAR_TRANSPORTE_ID = (MobileBy.ID, "")
    MENSAJE_TRANSPORTE_LISTO_ID = (MobileBy.ID, "")

    def ingreso_correo(self, correo):
        return True

    def ingreso_contrasena(self, contrasena):
        return True

    def clic_ingresar(self):
        return True

    def elegir_ruta(self, ruta):
        return True

    def seleccionar_comenzar_ruta(self):
        return True

    def visualizar_pantalla_ruta_finalizada(self):
        return True

    def producto_presente(self, producto):
        return True

    def efectivo_valido(self, total):
        return True

    def validar_total_transferencia(self, transferencia):
        return True

    def cheque_valido(self, efectivo):
        return True

    def validar_total_cheque(self, cheque):
        return True

    def credito_valido(self, credito):
        return True

    def rebajado_valido(self, rebajado):
        return True

    def boton_cerrar_transporte_presente(self):
        return True

    def mensaje_transporte_listo(self, mensaje):
        return True
