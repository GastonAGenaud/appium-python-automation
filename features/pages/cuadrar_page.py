from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class CuadrarPage(Page):
    texto_ruta_fecha = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-route"]')
    texto25Clientes = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-quantity"]')
    rutaComenzar = (MobileBy.ACCESSIBILITY_ID, ', Ruta comenzada')
    textoRutaEntregada = (MobileBy.XPATH, '//android.widget.TextView[@text="Entregada"]')
    confirmar_btn = (MobileBy.ACCESSIBILITY_ID, 'Confirmar')
    no_hay_productos_rebajados_texto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="HeaderCustom"]')
    total_esperado_precio = (MobileBy.XPATH, '(//android.widget.TextView[@text="$811.371"])[1]')
    total_recaudado_precio = (MobileBy.XPATH, '(//android.widget.TextView[@text="$811.371"])[2]')
    total_rebajado_precio = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-reba-amount"]')
    monto_transferencia = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-transfer"]')
    monto_efectivo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-cash"]')
    monto_cheque = (MobileBy.XPATH, '(//android.widget.TextView[@text="$811.371"])[3]')
    monto_credito = (MobileBy.XPATH, '(//android.widget.TextView[@text="$0"])[3]')
    cerrar_transporte_boton = (MobileBy.ACCESSIBILITY_ID, 'Cerrar transporte')
    mensaje_transporte_listo = (MobileBy.XPATH, '//android.widget.TextView[@text="Transporte listo"]')
    factura_entregada_a = (MobileBy.XPATH, '(//android.widget.TextView[@text="Entregada"])[1]')
    factura_entregada_b = (MobileBy.XPATH, '(//android.widget.TextView[@text="Entregada"])[2]')

    def click_cerrar_transporte_btn(self):
        self.click_on_element(self.cerrar_transporte_boton)

    def validar_texto_ruta_fecha(self):
        self.implicit_wait_visible(self.texto_ruta_fecha)
        texto_fecha = self.find_element(self.texto_ruta_fecha).is_displayed()
        return texto_fecha

    def validar_texto_25_clientes(self):
        self.implicit_wait_visible(self.texto25Clientes)
        return self.find_element(self.texto25Clientes).is_displayed()

    def validar_mensaje_comenzar(self):
        self.implicit_wait_visible(self.rutaComenzar)
        return self.find_element(self.rutaComenzar).is_displayed()

    def validar_texto_entregada(self):
        self.implicit_wait_visible(self.textoRutaEntregada)
        texto_entregado = self.find_element(self.textoRutaEntregada).is_displayed()
        return texto_entregado

    def validar_texto_no_hay_producto(self):
        self.implicit_wait_visible(self.no_hay_productos_rebajados_texto)
        texto_no_hay_producto = self.find_element(self.no_hay_productos_rebajados_texto).is_displayed()
        return texto_no_hay_producto

    def validar_precio_total_esperado(self):
        self.implicit_wait_visible(self.total_esperado_precio)
        total_esperado = self.find_element(self.total_esperado_precio).is_displayed()
        return total_esperado

    def validar_precio_total_recaudado(self):
        self.implicit_wait_visible(self.total_recaudado_precio)
        total_recaudado = self.find_element(self.total_recaudado_precio).is_displayed()
        return total_recaudado

    def validar_precio_total_rebajado(self):
        self.implicit_wait_visible(self.total_rebajado_precio)
        total_rebajado = self.find_element(self.total_rebajado_precio).is_displayed()
        return total_rebajado

    def valido_monto_transferencia(self):
        self.implicit_wait_visible(self.monto_transferencia)
        monto_abonado = self.find_element(self.monto_transferencia).is_displayed()
        return monto_abonado

    def valido_monto_efectivo(self):
        self.implicit_wait_visible(self.monto_efectivo)
        monto_abonado = self.find_element(self.monto_efectivo).is_displayed()
        return monto_abonado

    def valido_monto_cheque(self):
        self.implicit_wait_visible(self.monto_cheque)
        monto_abonado = self.find_element(self.monto_cheque).is_displayed()
        return monto_abonado

    def valido_monto_credito(self):
        self.implicit_wait_visible(self.monto_credito)
        monto_abonado = self.find_element(self.monto_credito).is_displayed()
        return monto_abonado

    def valido_mensaje_de_transporte_listo(self):
        self.implicit_wait_visible(self.mensaje_transporte_listo)
        mensaje = self.find_element(self.mensaje_transporte_listo).is_displayed()
        return mensaje

    def valido_factura_entregada_a(self):
        self.implicit_wait_visible(self.factura_entregada_a)
        factura_entregada = self.find_element(self.factura_entregada_a).is_displayed()
        return factura_entregada

    def valido_factura_entregada_b(self):
        self.implicit_wait_visible(self.factura_entregada_b)
        factura_entregada = self.find_element(self.factura_entregada_b).is_displayed()
        return factura_entregada
