import re

from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class RevisarPedidoPage(Page):
    el_deseo_spa_pedido = (
        MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Productos , 16, Transferencia, $866.455"]')
    el_deseo_spa_titulo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="address"]')
    precio_del_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 866.455"]')
    productos_del_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="10"]')
    productos_del_pedido_dos = (MobileBy.XPATH, '//android.widget.TextView[@text="6"]')
    google_maps_opcion = (MobileBy.ACCESSIBILITY_ID, 'Ver mapa')
    anular_pedido_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Anular pedido"]')
    entregar_btn = (MobileBy.ACCESSIBILITY_ID, 'Entregar')
    coca_cola_zero_pack = (MobileBy.XPATH, '//android.widget.TextView[@text="Coca Cola Zero 1.5 LT Pack 1 "]')
    precio_unitario_coca_zero = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 2.000 "]')
    precio_final_coca_zero = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 40.000 "]')
    precio_total_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 508.147"]')
    restar_btn = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="-"])[1]')
    agregar_btn = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="+"])[1]')
    factura_del_pedido = (MobileBy.XPATH, '(//android.widget.TextView[@text="Factura N° 404145531"])[1]')
    sprite_MidCal_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="Sprite MidCal PT250cc x6 "]')
    benedictino_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="Benedictino S/G PT6.5 x 2 Cilindrico "]')
    fanta_midcal_express_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="Fanta MidCal Express 237cc x 24 "]')
    precio_unitario_sprite_midCal = (MobileBy.XPATH, '//android.widget.TextView[@text="$65.064"]')
    precio_unitario_fanta = (MobileBy.XPATH, '//android.widget.TextView[@text="$66.210"]')
    precio_unitario_benedictino = (MobileBy.XPATH, '//android.widget.TextView[@text="$376.873"]')
    cantidad_pack_coca_cola = (MobileBy.XPATH, '//android.widget.EditText[@resource-id="stepperTextCustom" and @text="4"]')
    cantidad_pack_fanta = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-planned-units" and @text="de 2 "]')
    cantidad_pack_sprite = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-planned-units" and '
                                            '@text="de 1 "]')
    cantidad_pack_benedictino = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-planned-units" and '
                                                 '@text="de 7 "]')
    precio_final_sprite = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-amount-total" and @text="$ 65.064 "]')
    precio_final_fanta = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-amount-total" and @text="$ 66.210 "]')
    precio_final_benedictino = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-amount-total" and @text="$ 66.210 "]')
    retornar_pedido_btn = (MobileBy.XPATH, '//android.widget.TextView[@text="Retornar pedido"]')
    sprite_midcal_express_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="Sprite MidCal PT250cc x6 "]')
    #benedictino_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="Benedictino S/G PT6.5 x 2 Cilindrico "]')
    benedictino_precio_unitario = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-unit-price" and @text="$ 53.839 "]')
    fanta_precio_unitario = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-unit-price" and @text="$ 33.105 "]')

    def valido_pedido_el_deseo_spa(self):
        self.implicit_wait_visible(self.el_deseo_spa_titulo)
        valido_deseo_spa = self.find_element(self.el_deseo_spa_titulo).is_displayed()
        return valido_deseo_spa

    def valido_precio_del_pedido(self):
        self.implicit_wait_visible(self.precio_del_pedido)
        valido_precio = self.find_element(self.precio_del_pedido).is_displayed()
        return valido_precio

    def valido_cantidad_de_productos(self):
        self.implicit_wait_visible(self.productos_del_pedido)
        self.implicit_wait_visible(self.productos_del_pedido_dos)

        cantidad_de_productos = self.find_element(self.productos_del_pedido).is_displayed()
        cantidad_de_productos_dos = self.find_element(self.productos_del_pedido_dos).is_displayed()

        return cantidad_de_productos and cantidad_de_productos_dos

    def valido_opcion_google_maps(self):
        self.implicit_wait_visible(self.google_maps_opcion)
        google_maps = self.find_element(self.google_maps_opcion).is_displayed()
        return google_maps

    def valido_numero_de_factura(self, factura):
        self.implicit_wait_visible(self.google_maps_opcion)
        numero_de_factura = self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@text="Factura N° {factura}"]')
        return numero_de_factura

    def selecciono_la_factura(self):
        self.click_on_element(self.factura_del_pedido)

    #def selecciono_la_factura_deseo_spa(self):
    #    self.click_on_element(self.factura_del_pedido_deseo_spa)

    def click_anular_pedido_btn(self):
        self.click_on_element(self.anular_pedido_btn)

    def click_retornar_pedido_btn(self):
        self.click_on_element(self.retornar_pedido_btn)

    def click_entregar_btn(self):
        self.click_on_element(self.entregar_btn)

    def click_entregar_boton(self):
        self.click_on_element(self.entregar_btn)

    def valido_producto_coca_zero(self):
        self.implicit_wait_visible(self.coca_cola_zero_pack)
        coca_zero = self.find_element(self.coca_cola_zero_pack).is_displayed()
        return coca_zero

    def valido_producto_sprite_MidCal(self):
        self.implicit_wait_visible(self.sprite_MidCal_pedido)
        coca_cola = self.find_element(self.sprite_MidCal_pedido).is_displayed()
        return coca_cola

    def benedictino_cilindrico_pedido(self):
        self.implicit_wait_visible(self.benedictino_pedido)
        fanta = self.find_element(self.benedictino_pedido).is_displayed()
        return fanta

    def valido_producto_fanta_express(self):
        self.implicit_wait_visible(self.fanta_midcal_express_pedido)
        fanta_express = self.find_element(self.fanta_midcal_express_pedido).is_displayed()
        return fanta_express

    def valido_producto_sprite_express(self):
        self.implicit_wait_visible(self.sprite_midcal_express_pedido)
        sprite_express = self.find_element(self.sprite_midcal_express_pedido).is_displayed()
        return sprite_express

    #def valido_producto_benedictino(self):
    #    self.implicit_wait_visible(self.benedictino_pedido)
    #    benedictino_express = self.find_element(self.benedictino_pedido).is_displayed()
    #    return benedictino_express

    def valido_precio_unitario(self):
        self.implicit_wait_visible(self.precio_unitario_coca_zero)
        precio_unitario = self.find_element(self.precio_unitario_coca_zero).is_displayed()
        return precio_unitario

    def valido_precio_unitario_sprite_midCal(self):
        self.implicit_wait_visible(self.precio_unitario_sprite_midCal)
        precio_unitario = self.find_element(self.precio_unitario_sprite_midCal).is_displayed()
        return precio_unitario

    def valido_precio_unitario_fanta(self):
        self.implicit_wait_visible(self.precio_unitario_fanta)
        precio_unitario = self.find_element(self.precio_unitario_fanta).is_displayed()
        return precio_unitario

    def valido_precio_unitario_benedictino(self):
        self.implicit_wait_visible(self.precio_unitario_benedictino)
        precio_unitario = self.find_element(self.precio_unitario_benedictino).is_displayed()
        return precio_unitario

    def valido_benedictino_precio_unitario(self):
        self.implicit_wait_visible(self.benedictino_precio_unitario)
        benedictino_precio_unitario = self.find_element(self.benedictino_precio_unitario).is_displayed()
        return benedictino_precio_unitario

    def valido_fanta_MidCal_precio_unitario(self):
        self.implicit_wait_visible(self.fanta_precio_unitario)
        fanta_midcal_precio_unitario = self.find_element(self.fanta_precio_unitario).is_displayed()
        return fanta_midcal_precio_unitario

    def valido_cantidad_pack_coca_cola(self):
        self.implicit_wait_visible(self.cantidad_pack_coca_cola)
        cantidad_pack = self.find_element(self.cantidad_pack_coca_cola).is_displayed()
        return cantidad_pack

    def valido_cantidad_pack_fanta(self):
        self.implicit_wait_visible(self.cantidad_pack_fanta)
        cantidad_pack = self.find_element(self.cantidad_pack_fanta).is_displayed()
        return cantidad_pack

    def valido_cantidad_pack_fanta_express(self):
        self.implicit_wait_visible(self.cantidad_pack_fanta_express)
        cantidad_pack = self.find_element(self.cantidad_pack_fanta_express).is_displayed()
        return cantidad_pack

    def valido_cantidad_pack_sprite_express(self):
        self.implicit_wait_visible(self.cantidad_pack_sprite)
        cantidad_pack = self.find_element(self.cantidad_pack_sprite).is_displayed()
        return cantidad_pack

    def valido_cantidad_pack_benedictino(self):
        self.implicit_wait_visible(self.cantidad_pack_benedictino)
        cantidad_pack = self.find_element(self.cantidad_pack_benedictino).is_displayed()
        return cantidad_pack

    def valido_precio_final(self):
        self.implicit_wait_visible(self.precio_final_coca_zero)
        precio_final = self.find_element(self.precio_final_coca_zero).is_displayed()
        return precio_final

    def valido_precio_final_sprite(self):
        self.implicit_wait_visible(self.precio_final_sprite)
        precio_final = self.find_element(self.precio_final_sprite).is_displayed()
        return precio_final

    def valido_precio_final_fanta(self):
        self.implicit_wait_visible(self.precio_final_fanta)
        precio_final = self.find_element(self.precio_final_fanta).is_displayed()
        return precio_final

    def valido_precio_final_benedictino(self):
        self.implicit_wait_visible(self.precio_final_benedictino)
        precio_final = self.find_element(self.precio_final_benedictino).is_displayed()
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

    def valido_comparacion_de_precio(self):
        producto_1 = self.driver.find_element(MobileBy.XPATH, '(//android.widget.TextView[@resource-id="title-amount-total"])[1]')
        precio_producto_1 = producto_1.text
        solo_numeros_1 = re.sub(r'\D', '', precio_producto_1)
        producto1 = int(solo_numeros_1)

        producto_2 = self.driver.find_element(MobileBy.XPATH, '(//android.widget.TextView[@resource-id="title-amount-total"])[2]')
        precio_producto_2 = producto_2.text
        solo_numeros_2 = re.sub(r'\D', '', precio_producto_2)
        producto2 = int(solo_numeros_2)

        producto_3 = self.driver.find_element(MobileBy.XPATH, '(//android.widget.TextView[@resource-id="title-amount-total"])[3]')
        precio_producto_3 = producto_3.text
        solo_numeros_3 = re.sub(r'\D', '', precio_producto_3)
        producto3 = int(solo_numeros_3)

        valor_total = self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@resource-id="total-price"]')
        precio_producto_total = valor_total.text
        solo_numeros_total = re.sub(r'\D', '', precio_producto_total)
        productoTotal = int(solo_numeros_total)

        comparacion_de_precios = (producto1 + producto2 + producto3) == productoTotal
        assert comparacion_de_precios, "La comparación de precios no es válida"
        return True
