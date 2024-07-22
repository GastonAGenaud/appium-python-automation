import re
from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class RevisarPedidoPage(Page):
    el_deseo_spa_titulo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="address"]')
    like_eat_foods_spa_titulo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-location"]')
    precio_del_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 866.455"]')
    productos_del_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="10"]')
    productos_del_pedido_dos = (MobileBy.XPATH, '//android.widget.TextView[@text="6"]')
    google_maps_opcion = (MobileBy.ACCESSIBILITY_ID, 'Ver mapa')
    anular_pedido_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Anular pedido"]')
    entregar_btn = (MobileBy.ACCESSIBILITY_ID, 'Entregar')
    precio_total_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 508.147"]')
    restar_btn = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="-"])[1]')
    agregar_btn = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="+"])[1]')
    factura_del_pedido = (MobileBy.XPATH, '(//android.widget.TextView[@text="Factura N° 404145531"])[1]')
    factura_del_pedido2 = (MobileBy.XPATH, '(//android.widget.TextView[@text="Factura N° 404145531"])[2]')
    factura_del_pedido_foods_spa = (MobileBy.XPATH, '(//android.widget.TextView[@text="Factura N° 404145535"])[1]')
    factura_del_pedido_foods_spa2 = (MobileBy.XPATH, '(//android.widget.TextView[@text="Factura N° 404145535"])[2]')
    factura_del_pedido_erbi_uno = (MobileBy.XPATH, '//android.widget.TextView[@text="Factura N° 83908330"]')
    factura_del_pedido_erbi_dos = (MobileBy.XPATH, '//android.widget.TextView[@text="Factura N° 8390812"]')
    sprite_MidCal_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="Sprite MidCal PT250cc x6 "]')
    benedictino_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="Benedictino S/G PT6.5 x 2 Cilindrico "]')
    fanta_midcal_express_pedido = (
        MobileBy.XPATH, '//android.widget.TextView[@text="Fanta MidCal Express 237cc x 24 "]')
    precio_unitario_sprite_midCal = (MobileBy.XPATH, '//android.widget.TextView[@text="$65.064"]')
    precio_unitario_fanta = (MobileBy.XPATH, '//android.widget.TextView[@text="$66.210"]')
    precio_unitario_benedictino = (MobileBy.XPATH, '//android.widget.TextView[@text="$376.873"]')
    cantidad_pack_fanta = (
        MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-planned-units" and @text="de 2 "]')
    cantidad_pack_sprite = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-planned-units" and '
                                            '@text="de 1 "]')
    cantidad_pack_benedictino = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-planned-units" and '
                                                 '@text="de 7 "]')
    precio_final_sprite = (
        MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-amount-total" and @text="$ 65.064 "]')
    precio_final_fanta = (
        MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-amount-total" and @text="$ 66.210 "]')
    precio_final_benedictino = (
        MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-amount-total" and @text="$ 66.210 "]')
    retornar_factura_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Retornar factura"]')
    retornar_todo_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Retornar todo"]')
    sprite_midcal_express_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="Sprite MidCal PT250cc x6 "]')
    benedictino_precio_unitario = (
        MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-unit-price" and @text="$ 53.839 "]')
    fanta_precio_unitario = (
        MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-unit-price" and @text="$ 33.105 "]')
    nota_de_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="- $ 25.000"]')
    metodo_de_pago = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="formatted-product"]')
    metodo_de_pago_titulo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="HeaderCustom"]')
    transferencia_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="Transferencia"]')
    efectivo_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="Efectivo"]')
    mas_de_un_metodo_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="Con más de un método de pago"]')
    transferencia_texto = (MobileBy.XPATH, '//android.widget.TextView[@text="Transferencia"]')
    validar_metodo_pago_mensaje = (
        MobileBy.XPATH, '//android.view.ViewGroup[@content-desc=", Método de pago editado"]')
    check_efectivo = (MobileBy.XPATH, '(//android.widget.CheckBox[@resource-id="check-ContainerTwoPage"])['
                                      '1]/android.view.ViewGroup/android.view.ViewGroup')
    check_transferencia = (MobileBy.XPATH, '(//android.widget.CheckBox[@resource-id="check-ContainerTwoPage"])['
                                           '2]/android.view.ViewGroup/android.view.ViewGroup')
    campo_texto_efectivo = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[1]')
    campo_texto_transferencia = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[2]')
    mensaje_cheche_no_poder_usar = (MobileBy.XPATH, '//android.widget.TextView[@text="No puedes usar un cheque como '
                                                    'parte de pago. Solo se acepta para el total."]')
    vuelta = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-home-1"]')

    def cheque_mensaje_no_poder_usar(self):
        self.implicit_wait_visible(self.mensaje_cheche_no_poder_usar)
        valido_mensaje_sector_cheque = self.find_element(self.mensaje_cheche_no_poder_usar).is_displayed()
        return valido_mensaje_sector_cheque

    def seleccionar_check_transferencia(self):
        self.implicit_wait_visible(self.check_transferencia)
        valido_check_transferencia = self.find_element(self.check_transferencia).is_displayed()
        self.click_on_element(self.check_transferencia)
        return valido_check_transferencia

    def seleccionar_check_efectivo(self):
        self.implicit_wait_visible(self.check_efectivo)
        valido_check_efectivo = self.find_element(self.check_efectivo).is_displayed()
        self.click_on_element(self.check_efectivo)
        return valido_check_efectivo

    def metodo_pago_mensaje(self):
        self.implicit_wait_visible(self.validar_metodo_pago_mensaje)
        valido_mensaje_pago = self.find_element(self.validar_metodo_pago_mensaje).is_displayed()
        return valido_mensaje_pago

    def valido_pedido_el_deseo_spa(self):
        self.implicit_wait_visible(self.el_deseo_spa_titulo)
        valido_deseo_spa = self.find_element(self.el_deseo_spa_titulo).is_displayed()
        return valido_deseo_spa

    def click_like_eat_foods_spa_btn(self):
        self.click_on_element(self.like_eat_foods_spa_titulo)

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

    def selecciono_la_factura(self):
        self.click_on_element(self.factura_del_pedido)

    def selecciono_la_factura_erbi_A(self):
        self.click_on_element(self.factura_del_pedido_erbi_uno)

    def selecciono_la_factura_erbi_B(self):
        self.click_on_element(self.factura_del_pedido_erbi_dos)

    def selecciono_la_factura_foods_spa(self):
        self.click_on_element(self.factura_del_pedido_foods_spa)

    def selecciono_la_factura_foods_spa2(self):
        self.click_on_element(self.factura_del_pedido_foods_spa2)

    def selecciono_la_factura2(self):
        self.click_on_element(self.factura_del_pedido2)

    def click_anular_pedido_btn(self):
        self.click_on_element(self.anular_pedido_btn)

    def click_retornar_factura_btn(self):
        self.click_on_element(self.retornar_factura_btn)

    def click_retornar_todo_btn(self):
        self.click_on_element(self.retornar_todo_btn)

    def click_entregar_btn(self):
        self.click_on_element(self.entregar_btn)

    def click_entregar_boton(self):
        self.click_on_element(self.entregar_btn)

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

    def valido_cantidad_pack_fanta(self):
        self.implicit_wait_visible(self.cantidad_pack_fanta)
        cantidad_pack = self.find_element(self.cantidad_pack_fanta).is_displayed()
        return cantidad_pack

    def valido_cantidad_pack_sprite_express(self):
        self.implicit_wait_visible(self.cantidad_pack_sprite)
        cantidad_pack = self.find_element(self.cantidad_pack_sprite).is_displayed()
        return cantidad_pack

    def valido_cantidad_pack_benedictino(self):
        self.implicit_wait_visible(self.cantidad_pack_benedictino)
        cantidad_pack = self.find_element(self.cantidad_pack_benedictino).is_displayed()
        return cantidad_pack

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
        producto_1 = self.driver.find_element(MobileBy.XPATH,
                                              '(//android.widget.TextView[@resource-id="title-amount-total"])[1]')
        precio_producto_1 = producto_1.text
        solo_numeros_1 = re.sub(r'\D', '', precio_producto_1)
        producto1 = int(solo_numeros_1)

        producto_2 = self.driver.find_element(MobileBy.XPATH,
                                              '(//android.widget.TextView[@resource-id="title-amount-total"])[2]')
        precio_producto_2 = producto_2.text
        solo_numeros_2 = re.sub(r'\D', '', precio_producto_2)
        producto2 = int(solo_numeros_2)

        producto_3 = self.driver.find_element(MobileBy.XPATH,
                                              '(//android.widget.TextView[@resource-id="title-amount-total"])[3]')
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

    def valido_nota_pedido(self):
        self.implicit_wait_visible(self.nota_de_pedido)
        valido_monto = self.find_element(self.nota_de_pedido).is_displayed()
        return valido_monto

    def click_metodo_de_pago(self):
        self.click_on_element(self.metodo_de_pago)

    def valido_titulo_metodo_de_pago(self):
        self.implicit_wait_visible(self.metodo_de_pago_titulo)
        titulo = self.find_element(self.metodo_de_pago_titulo).is_displayed()
        return titulo

    def valido_transferencia_opcion(self):
        self.implicit_wait_visible(self.transferencia_txt)
        texto = self.find_element(self.transferencia_txt).is_displayed()
        return texto

    def click_transferencia_opcion(self):
        self.click_on_element(self.transferencia_txt)

    def valido_efectivo_opcion(self):
        self.implicit_wait_visible(self.efectivo_txt)
        texto = self.find_element(self.efectivo_txt).is_displayed()
        return texto

    def click_efectivo_opcion(self):
        self.click_on_element(self.efectivo_txt)

    def valido_mas_de_un_metodo_opcion(self):
        self.implicit_wait_visible(self.mas_de_un_metodo_txt)
        texto = self.find_element(self.mas_de_un_metodo_txt).is_displayed()
        return texto

    def click_mas_de_un_metodo_opcion(self):
        self.click_on_element(self.mas_de_un_metodo_txt)

    def valido_metodo_seleccionado(self):
        self.implicit_wait_visible(self.transferencia_texto)
        metodo_seleccionado = self.find_element(self.transferencia_texto).is_displayed()
        return metodo_seleccionado

    def ingreso_montos_transferencia_efectivo(self):
        total = self.driver.find_element(MobileBy.XPATH,
                                              '//android.widget.TextView[@resource-id="title-CardAmount-a"]')
        precio_total = total.text
        solo_numeros = re.sub(r'\D', '', precio_total)
        total = int(solo_numeros)
        monto_indivivual = total / 2

        self.click_on_element(self.campo_texto_efectivo)
        self.input(monto_indivivual, self.campo_texto_efectivo)

        self.click_on_element(self.campo_texto_transferencia)
        self.input(monto_indivivual, self.campo_texto_transferencia)

    def click_vuelta_1(self):
        self.click_on_element(self.vuelta)

