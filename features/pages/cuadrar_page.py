# -*- coding: utf-8 -*-

class RoutePage:
    def __init__(self, driver):
        self.driver = driver

    def seleccionar_ruta(self, nombre_ruta):
        pass

    def hacer_clic_comenzar_ruta(self):
        pass


class FinalizedRoutePage:
    def __init__(self, driver):
        self.driver = driver

    def validar_producto_presente(self, nombre_producto):
        pass

    def validar_total(self, cantidad, total_esperado):
        pass

    def validar_botón_cerrar_transporte_presente(self):
        pass

    def validar_mensaje_transporte_listo(self, mensaje_esperado):
        pass
