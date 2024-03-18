# -*- coding: utf-8 -*-

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def ingresar_correo(self, correo):
        pass

    def ingresar_contraseña(self, contraseña):
        pass

    def hacer_clic_ingresar(self):
        pass


class InvoicePage:
    def __init__(self, driver):
        self.driver = driver

    def visualizar_factura(self, numero_factura):
        pass

    def clic_anular_pedido(self):
        pass


class CancellationReasonPage:
    def __init__(self, driver):
        self.driver = driver

    def is_open(self):
        pass

    def visualizar_pantalla_anulacion(self):
        pass

    def is_reason_present(self, motivo):
        pass

    def is_send_reason_button_present(self):
        pass

    def clic_enviar_motivo(self):
        pass

    def verificar_envio_motivo(self):
        pass


class RouteSelectionPage:
    def __init__(self, driver):
        self.driver = driver

    def seleccionar_nombre(self, nombre):
        pass

    def clic_anulados(self):
        pass


class CancelledOrdersPage:
    def __init__(self, driver):
        self.driver = driver

    def is_previous_route_present(self, id_ruta):
        pass

    def is_text_present(self, texto):
        pass

    def is_start_route_button_present(self):
        pass


class ReturnOrdersPage:
    def __init__(self, driver):
        self.driver = driver

    def visualizar_pantalla_retomar_pedidos(self):

        pass

    def validar_ruta_pedido(self, ruta):
        pass

    def validar_presencia_boton_retomar_pedido(self):
        pass

    def clic_retomar_pedido(self):
        pass

