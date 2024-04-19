from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class RevisarPedidoPage(Page):
    avenida_las_condes_pedido = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Productos , 25, Método no reconocido, $40.000"]')
    renca_pedido = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Productos , 15, Método no reconocido, $35.000"]')
    pudahuel_pedido = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Productos , 20, Método no reconocido, $50.000"]')
    avenida_las_condes_titulo = (MobileBy.XPATH, '(//android.widget.TextView[@text="Avenida Las Condes, "])[2]')
    pudahuel_titulo = (MobileBy.XPATH, '(//android.widget.TextView[@text="Pudahuel, Santiago, "])[2]')
    precio_del_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 2.000"]')
    productos_del_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="20"]')
    google_maps_opcion = (MobileBy.XPATH, '//android.widget.TextView[@text="Ver mapa"]')
    anular_pedido_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Anular pedido"]')
    entregar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Entregar"]')
    coca_cola_zero_pack = (MobileBy.XPATH, '//android.widget.TextView[@text="Coca Cola Zero 1.5 LT Pack 1 "]')
    precio_unitario_coca_zero = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 2.000 "]')
    precio_final_coca_zero = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 40.000 "]')
    precio_total_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 2.000"]')
    restar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="-"]')
    agregar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="+"]')

    def click_avenida_las_condes_btn(self):
        self.click_on_element(self.avenida_las_condes_pedido)

    def click_pudahuel_btn(self):
        self.click_on_element(self.pudahuel_pedido)

    def click_renca_btn(self):
        self.click_on_element(self.renca_pedido)

    def valido_pedido_avenida_las_condes(self):
        self.implicit_wait_visible(self.avenida_las_condes_titulo)
        valido_avenida_las_condes = self.find_element(self.avenida_las_condes_titulo).is_displayed()
        return valido_avenida_las_condes

    def valido_pedido_pudahuel(self):
        self.implicit_wait_visible(self.avenida_las_condes_titulo)
        valido_pudahuel = self.find_element(self.avenida_las_condes_titulo).is_displayed()
        return valido_pudahuel

    def valido_precio_del_pedido(self, precio):
        self.implicit_wait_visible(self.precio_del_pedido)
        precio = self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="{precio}"]').is_displayed()
        return precio

    def valido_cantidad_de_productos(self, producto):
        self.implicit_wait_visible(self.productos_del_pedido)
        cantidad_de_productos = self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="{producto}"]').is_displayed()
        return cantidad_de_productos

    def valido_opcion_google_maps(self):
        self.implicit_wait_visible(self.google_maps_opcion)
        google_maps = self.find_element(self.google_maps_opcion).is_displayed()
        return google_maps

    def valido_numero_de_factura(self, factura):
        self.implicit_wait_visible(self.google_maps_opcion)
        numero_de_factura = self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="Factura N° {factura}"]')
        return numero_de_factura

    def selecciono_la_factura(self, factura):
        self.click_on_element(self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="Factura N° {factura}"]'))

    def click_anular_pedido_btn(self):
        self.click_on_element(self.anular_pedido_btn)

    def click_entregar_btn(self):
        self.click_on_element(self.entregar_btn)

    def valido_producto_coca_zero(self):
        self.implicit_wait_visible(self.coca_cola_zero_pack)
        coca_zero = self.find_element(self.coca_cola_zero_pack).is_displayed()
        return coca_zero

    def valido_precio_unitario(self):
        self.implicit_wait_visible(self.precio_unitario_coca_zero)
        precio_unitario = self.find_element(self.precio_unitario_coca_zero).is_displayed()
        return precio_unitario

    def valido_precio_final(self):
        self.implicit_wait_visible(self.precio_final_coca_zero)
        precio_final = self.find_element(self.precio_final_coca_zero).is_displayed()
        return precio_final

    def valido_precio_total(self):
        self.implicit_wait_visible(self.precio_total_pedido)
        precio_total = self.find_element(self.precio_total_pedido).is_displayed()
        return precio_total

    def valido_restar_btn(self):
        self.implicit_wait_visible(self.restar_btn)
        valido_restar = self.find_element(self.restar_btn).is_displayed()
        return valido_restar

    def valido_agregar_btn(self):
        self.implicit_wait_visible(self.agregar_btn)
        valido_agregar = self.find_element(self.agregar_btn).is_displayed()
        return valido_agregar
