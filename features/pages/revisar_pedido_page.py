import re
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy
from features.pages.ux_page import UXPage


class RevisarPedidoPage(Page):
    el_deseo_spa_titulo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="address"]')
    like_eat_foods_spa_titulo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-location"]')
    precio_del_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="$ 35.000"]')
    productos_del_pedido = (MobileBy.XPATH, '//android.widget.TextView[@text="10 caj - 10 pac"]')
    productos_del_pedido_dos = (MobileBy.XPATH, '//android.widget.TextView[@text="10 caj - 10 pac"]')
    google_maps_opcion = (MobileBy.ACCESSIBILITY_ID, 'Ver mapa')
    anular_pedido_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Anular pedido"]')
    aceptar_btn = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Aceptar"]')
    precio_total_pedido = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="total-price"]')
    precio_total_metodo = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-CardAmount-a"]')
    restar_btn = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="-"])[1]')
    agregar_btn = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="+"])[1]')
    factura_del_pedido = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Factura N° 812345672, Productos, '
                                          '10 caj - 10 pac, Transferencia/Efectivo, $20.000"]')
    factura_del_pedido2 = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Préstamo de envases N° 812345671, '
                                           'Cantidad, 10 caj, Cheque, $15.000"]')
    factura_del_pedido_foods_spa = (MobileBy.XPATH, '(//android.widget.TextView[@text="Factura N° 404145535"])[1]')
    factura_del_pedido_foods_spa2 = (MobileBy.XPATH, '(//android.widget.TextView[@text="Factura N° 404145535"])[2]')
    factura_del_pedido_erbi_uno = (MobileBy.XPATH, '//android.widget.TextView[@text="Factura N° 83908330"]')
    factura_del_pedido_erbi_dos = (MobileBy.XPATH, '//android.widget.TextView[@text="Factura N° 8390812"]')
    coca_cola_sin_azucar = (MobileBy.XPATH, '//android.widget.TextView[@text="Coca Cola Sin Azucar LT350cc x 6 "]')
    andina_damasco = (MobileBy.XPATH, '//android.widget.TextView[@text="Andina Nectar Damasco PT1,5 x 6 "]')
    nordic_zero_pedido = (
        MobileBy.XPATH, '//android.widget.TextView[@text="Nordic Zero Ginger Ale PT3,0 x 6 "]')
    precio_unitario_sprite_midCal = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="title-unit-price"])[1]')
    precio_unitario_fanta = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="title-unit-price"])[2]')
    precio_unitario_benedictino = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="title-unit-price"])[3]')
    cantidad_pack_coca = (
        MobileBy.XPATH, '//android.widget.EditText[@resource-id="stepperTextCustom" and @text="10"]')
    cantidad_pack_nordic = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="stepperTextCustom"])[2]')
    cantidad_pack_andina = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="stepperTextCustom"])[3]')
    precio_final_coca = (
        MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-amount-total" and @text="$ 10.000"]')
    precio_final_nordic = (
        MobileBy.XPATH, '(//android.widget.TextView[@resource-id="title-amount-total"])[2]')
    precio_final_andina = (
        MobileBy.XPATH, '(//android.widget.TextView[@resource-id="title-amount-total"])[3]')
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
    transferencia_txt = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Transferencia"]')
    efectivo_txt = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Efectivo"]')
    mas_de_un_metodo_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="Con más de un método de pago"]')
    mas_de_un_metodo_xpath = (MobileBy.XPATH, '(//android.widget.RadioButton[@resource-id="RadioButtonConfirm"])['
                                              '3]/android.view.ViewGroup')
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
    vuelta = (MobileBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup')
    numero_telefono_local = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="phoneNumber"]')
    texto_cierre_local = (MobileBy.XPATH, '//android.widget.TextView[@text="Cierra a las 19:30"]')
    local_abierto = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="storeStatus"]')
    metodo_cheque = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="title-ContainerTwoPage-TypeCheck"]')

    def local_texto_abierto(self):
        self.implicit_wait_visible(self.local_abierto)
        return self.find_element(self.local_abierto).is_displayed()

    def cierre_de_local(self):
        self.implicit_wait_visible(self.texto_cierre_local)
        local_horario_visible = self.find_element(self.texto_cierre_local).is_displayed()
        return local_horario_visible

    def numero_telefono_local_visible(self):
        self.implicit_wait_visible(self.numero_telefono_local)
        numero_telefono_local_visible = self.find_element(self.numero_telefono_local).is_displayed()
        return numero_telefono_local_visible

    def seleccionar_check_transferencia(self):
        self.implicit_wait_visible(self.check_transferencia)
        self.click_on_element(self.check_transferencia)

    def seleccionar_check_efectivo(self):
        self.implicit_wait_visible(self.check_efectivo)
        self.click_on_element(self.check_efectivo)

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

    def click_aceptar_boton(self):
        self.click_on_element(self.aceptar_btn)

    def valido_producto_sprite_MidCal(self):
        self.implicit_wait_visible(self.sprite_MidCal_pedido)
        coca_cola = self.find_element(self.sprite_MidCal_pedido).is_displayed()
        return coca_cola

    def __init__(self, driver):
        super().__init__(driver)
        self.ux_page = UXPage(driver)  # Crear una instancia de UXPage

    def andina_damasco_pedido(self):
        self.implicit_wait_visible(self.andina_damasco)
        andina_damasco = self.find_element(self.andina_damasco).is_displayed()
        return andina_damasco

    def valido_producto_coca_cola(self):
        self.implicit_wait_visible(self.coca_cola_sin_azucar)
        coca_cola = self.find_element(self.coca_cola_sin_azucar).is_displayed()
        return coca_cola

    def valido_producto_nordic_zero(self):
        self.implicit_wait_visible(self.nordic_zero_pedido)
        nordic_zero = self.find_element(self.nordic_zero_pedido).is_displayed()
        return nordic_zero

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

    def valido_cantidad_pack_coca(self):
        self.implicit_wait_visible(self.cantidad_pack_coca)
        cantidad_pack = self.find_element(self.cantidad_pack_coca).is_displayed()
        return cantidad_pack

    def valido_cantidad_pack_nordic(self):
        self.implicit_wait_visible(self.cantidad_pack_nordic)
        cantidad_pack = self.find_element(self.cantidad_pack_nordic).is_displayed()
        return cantidad_pack

    def valido_cantidad_pack_andina(self):
        try:
            elemento = self.ux_page.scroll_down_until_element(self.cantidad_pack_andina)
            return True if elemento else False
        except NoSuchElementException:
            return False

    def valido_sector_cheque(self):
        self.implicit_wait_visible(self.metodo_cheque)
        metodo = self.find_element(self.metodo_cheque).is_displayed()
        return metodo

    def valido_precio_final_coca(self):
        self.implicit_wait_visible(self.precio_final_coca)
        precio_final = self.find_element(self.precio_final_coca).is_displayed()
        return precio_final

    def valido_precio_final_nordic(self):
        self.implicit_wait_visible(self.precio_final_nordic)
        precio_final = self.find_element(self.precio_final_nordic).is_displayed()
        return precio_final

    def valido_precio_final_andina(self):
        self.implicit_wait_visible(self.precio_final_andina)
        precio_final = self.find_element(self.precio_final_andina).is_displayed()
        return precio_final

    def valido_precio_total(self):
        self.implicit_wait_visible(self.precio_total_pedido)
        precio_total = self.find_element(self.precio_total_pedido).is_displayed()
        return precio_total

    def valido_precio_total_metodo(self):
        self.implicit_wait_visible(self.precio_total_metodo)
        precio_metodo_total = self.find_element(self.precio_total_metodo).is_displayed()
        return precio_metodo_total

    def valido_restar_btn(self):
        self.implicit_wait_visible(self.restar_btn)
        valido_restar = self.find_element(self.restar_btn).is_displayed()
        return valido_restar

    def valido_agregar_btn(self):
        self.implicit_wait_visible(self.agregar_btn)
        valido_agregar = self.find_element(self.agregar_btn).is_displayed()
        return valido_agregar

    def valido_contenido_factura(self):
        # Buscar y obtener el texto de los productos
        producto_1 = self.driver.find_element(MobileBy.XPATH,
                                              '//android.widget.TextView[@resource-id="title-amount-total" and '
                                              '@text="$ 10.000"]')
        precio_producto_1 = producto_1.text
        solo_numeros_1 = re.sub(r'\D', '', precio_producto_1)
        producto1 = int(solo_numeros_1)

        producto_2 = self.driver.find_element(MobileBy.XPATH,
                                              '(//android.widget.TextView[@resource-id="title-amount-total"])[2]')
        precio_producto_2 = producto_2.text
        solo_numeros_2 = re.sub(r'\D', '', precio_producto_2)
        producto2 = int(solo_numeros_2)

        # Scroll para encontrar el tercer producto
        producto_3 = self.driver.find_element(MobileBy.XPATH,
                                              '(//android.widget.TextView[@resource-id="title-amount-total"])[3]')
        precio_producto_3 = producto_3.text
        solo_numeros_3 = re.sub(r'\D', '', precio_producto_3)
        producto3 = int(solo_numeros_3)

        # Obtener el precio total
        valor_total = self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@resource-id="total-price"]')
        precio_producto_total = valor_total.text
        solo_numeros_total = re.sub(r'\D', '', precio_producto_total)
        productoTotal = int(solo_numeros_total)

        # Validación de la suma de los precios de los productos con el precio total
        comparacion_de_precios = (producto1 + producto2 + producto3) == productoTotal
        assert comparacion_de_precios, "La comparación de precios no es válida"

        # Validar que el precio total sea de "$ 20.000"
        expected_total = 20000
        assert productoTotal == expected_total, f"El precio total esperado es {expected_total}, pero se encontró {productoTotal}"

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
        self.implicit_wait_visible(self.efectivo_txt)
        self.click_on_element(self.efectivo_txt)

    def valido_mas_de_un_metodo_opcion(self):
        self.implicit_wait_visible(self.mas_de_un_metodo_txt)
        texto = self.find_element(self.mas_de_un_metodo_txt).is_displayed()
        return texto

    def click_mas_de_un_metodo_opcion(self):
        self.implicit_wait_visible(self.mas_de_un_metodo_txt)
        self.click_on_element(self.mas_de_un_metodo_txt)

    def mas_de_un_metodo(self):
        self.implicit_wait_visible(self.mas_de_un_metodo_xpath)
        self.click_on_element(self.mas_de_un_metodo_xpath)

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
        self.driver.hide_keyboard()
        self.click_on_element(self.campo_texto_transferencia)
        self.input(monto_indivivual, self.campo_texto_transferencia)
        self.driver.hide_keyboard()

    def click_vuelta_1(self):
        wait = WebDriverWait(self.driver, 10)
        self.vuelta = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup")
        ))
        self.vuelta.click()
