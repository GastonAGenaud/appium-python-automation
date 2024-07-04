from behave import given, when, then


# Paso para elegir una ruta
@when('elijo la ruta "{idRuta}"')
def usuario_elije_ruta(context, idRuta):
    if idRuta == "El Deseo SPA":
        context.app.ux_page.click_el_deseo_spa_btn()
    elif idRuta == "Erbi":
        context.app.revisar_pedido_page.click_erbi_btn()
    else:
        raise ValueError(f"No se encontró la ruta '{idRuta}'")


# Paso para validar la visualización del pedido para una ruta
@then('se valida que la visualizacion de pedido para la ruta "{idRuta}" sea correcta')
def visualizaciones_correcta_del_pedido(context, idRuta):
    assert bool(
        context.app.revisar_pedido_page.valido_pedido_el_deseo_spa()), f"Visualización incorrecta para la ruta '{idRuta}'"


# Paso para validar la visualización del monto de la transferencia
@then('valido la visualizacion del monto de la transferencia')
def valido_visualizacion_de_transferencia(context):
    assert bool(
        context.app.revisar_pedido_page.valido_precio_del_pedido()), "El monto de la transferencia no es visible"


# Paso para validar la visualización de la cantidad de los productos
@then('valido la visualizacion de la cantidad de los productos')
def valido_visualizacion_de_cantidad(context):
    assert bool(
        context.app.revisar_pedido_page.valido_cantidad_de_productos()), "La cantidad de productos no es visible"


# Paso para validar la presencia de una opción en Google Maps
@then('valido la presencia de la opcion "{maps}"')
def valido_google_maps(context, maps):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps()), f"La opción '{maps}' no está presente"


# Paso para seleccionar una factura por número
@when('selecciono la factura con numero "{factura}"')
def visualizo_la_factura(context, factura):
    if factura == "404145531":
        context.app.revisar_pedido_page.selecciono_la_factura()
    elif factura == "83908330":
        context.app.revisar_pedido_page.selecciono_la_factura_erbi_A()
    elif factura == "8390812":
        context.app.revisar_pedido_page.selecciono_la_factura_erbi_B()
    else:
        raise ValueError(f"No se encontró la factura con número '{factura}'")


# Paso para seleccionar una segunda factura por número
@when('selecciono la segunda factura con numero "{factura}"')
def visualizo_la_factura2(context, factura):
    if factura == "404145531":
        context.app.revisar_pedido_page.selecciono_la_factura2()
    else:
        raise ValueError(f"No se encontró la segunda factura con número '{factura}'")


# Paso para validar la confirmación de anulación del pedido
@then('valido que se muestre una confirmacion de anulacion del pedido')
def valido_anulacion_del_pedido(context):
    assert bool(
        context.app.revisar_pedido_page.valido_opcion_google_maps()), "La confirmación de anulación del pedido no es visible"


# Paso para validar un producto específico
@then('valido el producto "{producto}"')
def valido_producto(context, producto):
    if producto == "Sprite MidCal PT250cc x6":
        assert bool(
            context.app.revisar_pedido_page.valido_producto_sprite_MidCal()), f"El producto '{producto}' no está en la lista"
    elif producto == "Fanta MidCal Express 237cc x 24":
        assert bool(
            context.app.revisar_pedido_page.valido_producto_fanta_express()), f"El producto '{producto}' no está en la lista"
    elif producto == "Benedictino S/G PT6.5 x 2 Cilindrico":
        assert bool(
            context.app.revisar_pedido_page.benedictino_cilindrico_pedido()), f"El producto '{producto}' no está en la lista"
    else:
        raise ValueError(f"No se encontró el producto '{producto}'")


# Paso para validar el precio unitario de un producto
@then('valido el precio unitario "{precio}"')
def valido_precio_unitario(context, precio):
    if precio == "$65.064":
        assert bool(
            context.app.revisar_pedido_page.valido_precio_unitario_sprite_midCal()), f"El precio unitario '{precio}' no es correcto"
    elif precio == "$66.210":
        assert bool(
            context.app.revisar_pedido_page.valido_precio_unitario_fanta()), f"El precio unitario '{precio}' no es correcto"
    elif precio == "$376.873":
        assert bool(
            context.app.revisar_pedido_page.valido_precio_unitario_benedictino()), f"El precio unitario '{precio}' no es correcto"
    else:
        raise ValueError(f"No se encontró el precio '{precio}'")


# Paso para validar el precio unitario en la factura
@then('valido el precio unitario "{precio}" en la factura')
def valido_precio_unitario_factura(context, precio):
    if precio == "$ 65.064":
        assert bool(
            context.app.revisar_pedido_page.valido_producto_sprite_express()), f"El precio unitario '{precio}' en la factura no es correcto"
    elif precio == "$ 53.839":
        assert bool(
            context.app.revisar_pedido_page.valido_benedictino_precio_unitario()), f"El precio unitario '{precio}' en la factura no es correcto"
    elif precio == "$ 33.105":
        assert bool(
            context.app.revisar_pedido_page.valido_fanta_MidCal_precio_unitario()), f"El precio unitario '{precio}' en la factura no es correcto"
    else:
        raise ValueError(f"No se encontró el precio '{precio}' para validar en la factura")


# Paso para validar la cantidad de packs pedidos
@then('valido la cantidad de pack pedidos "{cantidad}"')
def valido_cantidad_pack(context, cantidad):
    if cantidad == "1":
        assert bool(
            context.app.revisar_pedido_page.valido_cantidad_pack_sprite_express()), f"La cantidad de pack '{cantidad}' no es correcta"
    elif cantidad == "2":
        assert bool(
            context.app.revisar_pedido_page.valido_cantidad_pack_fanta()), f"La cantidad de pack '{cantidad}' no es correcta"
    elif cantidad == "7":
        assert bool(
            context.app.revisar_pedido_page.valido_cantidad_pack_benedictino()), f"La cantidad de pack '{cantidad}' no es correcta"
    else:
        raise ValueError(f"No se encontró la cantidad de pack pedidos '{cantidad}'")


# Paso para validar el sector de botones de agregar y restar
@then('valido el sector de botones de agregar y restar')
def valido_sector_agregar_y_restar(context):
    assert bool(context.app.revisar_pedido_page.valido_restar_btn()), "El botón de restar no está visible"
    assert bool(context.app.revisar_pedido_page.valido_agregar_btn()), "El botón de agregar no está visible"


# Paso para validar el precio final de un producto
@then('valido el precio final "{precio}"')
def valido_precio_final(context, precio):
    if precio == "$ 65.064":
        assert bool(
            context.app.revisar_pedido_page.valido_precio_final_sprite()), f"El precio final '{precio}' no es correcto"
    elif precio == "$ 66.210":
        assert bool(
            context.app.revisar_pedido_page.valido_precio_final_fanta()), f"El precio final '{precio}' no es correcto"
    elif precio == "$ 376.873":
        assert bool(
            context.app.revisar_pedido_page.valido_precio_final_benedictino()), f"El precio final '{precio}' no es correcto"
    else:
        raise ValueError(f"No se encontró el precio final '{precio}'")


# Paso para validar el precio total
@then('valido que el precio total sea de "{precio}"')
def valido_total_precio(context, precio):
    assert bool(context.app.revisar_pedido_page.valido_precio_total()), f"El precio total '{precio}' no es correcto"


# Paso para validar la suma del precio de los productos
@then('valido que este correcta la suma del precio de los productos')
def valido_sea_correcto_precio(context):
    assert bool(
        context.app.revisar_pedido_page.valido_comparacion_de_precio()), "La suma del precio de los productos no es correcta"


# Paso para validar la nota de crédito
@then('valido que la nota de credito sea "{monto}"')
def valido_nota_de_credito(context, monto):
    assert bool(context.app.revisar_pedido_page.valido_nota_pedido()), f"La nota de crédito '{monto}' no es correcta"


# Paso para hacer clic en una opción de pago
@when('hago click en la opcion "{metodo}"')
def hago_click_opcion_metodo(context, metodo):
    context.app.revisar_pedido_page.click_metodo_de_pago()


# Paso para seleccionar un método de pago
@when('selecciono el metodo de pago "{metodo}"')
def selecciono_metodo_de_pago(context, metodo):
    if metodo == "Transferencia":
        context.app.revisar_pedido_page.click_transferencia_opcion()
    elif metodo == "Efectivo":
        context.app.revisar_pedido_page.click_efectivo_opcion()
    elif metodo == "Con mas de un metodo de pago":
        context.app.revisar_pedido_page.click_mas_de_un_metodo_opcion()
    else:
        raise ValueError(f"No se encontró el método de pago '{metodo}'")


# Paso para validar que un método de pago sea visible
@then('valido que sea visible el metodo de de pago "{metodo}"')
def valido_sea_visible_metodo(context, metodo):
    if metodo == "Transferencia":
        assert bool(
            context.app.revisar_pedido_page.valido_transferencia_opcion()), f"El método de pago '{metodo}' no está visible"
    elif metodo == "Efectivo":
        assert bool(
            context.app.revisar_pedido_page.valido_efectivo_opcion()), f"El método de pago '{metodo}' no está visible"
    elif metodo == "Con mas de un metodo de pago":
        assert bool(
            context.app.revisar_pedido_page.valido_mas_de_un_metodo_opcion()), f"El método de pago '{metodo}' no está visible"
    else:
        raise ValueError(f"No se encontró el método de pago '{metodo}'")


# Paso para validar que el método de pago fue seleccionado
@then('valido que el metodo de pago fue seleccionado')
def valido_sea_seleccionado_metodo(context):
    assert bool(context.app.revisar_pedido_page.valido_metodo_seleccionado()), "El método de pago no fue seleccionado"


# Paso para validar el mensaje de método de pago editado
@then('valido el mensaje "Metodo de pago editado"')
def valido_mensaje_pago_editado(context):
    assert bool(
        context.app.revisar_pedido_page.metodo_pago_mensaje()), "El mensaje 'Método de pago editado' no es visible"


# Paso para hacer clic en un check de pago
@when('hago click en el check "{metodo}"')
def valido_check_como_pagar(context, metodo):
    if metodo == "Efectivo":
        context.app.revisar_pedido_page.seleccionar_check_efectivo()
    elif metodo == "Transferencia":
        context.app.revisar_pedido_page.seleccionar_check_transferencia()
    else:
        raise ValueError(f"No se encontró el check de '{metodo}'")


# Paso para escribir un número en el campo de texto de un método de pago
@when('Escribo el numero total "{total}" y lo divido en dos partes para "{metodo1}" y "{metodo2}"')
def escribo_numero_dividido(context, total, metodo1, metodo2):
    # Convertir el total a un número
    valor_total = float(total.replace('$', '').replace(',', ''))

    # Dividir el total en dos partes
    valor_dividido = valor_total / 2

    if metodo1 == "Efectivo":
        # Escribir la primera mitad en Efectivo
        context.app.revisar_pedido_page.escribir_numero_efectivo(f"${valor_dividido:,.0f}")
    elif metodo1 == "Transferencia":
        # Escribir la primera mitad en Transferencia
        context.app.revisar_pedido_page.escribir_numero_transferencia(f"${valor_dividido:,.0f}")
    else:
        raise ValueError(f"No se encontró el método de pago '{metodo1}'")

    if metodo2 == "Efectivo":
        # Escribir la segunda mitad en Efectivo
        context.app.revisar_pedido_page.escribir_numero_efectivo(f"${valor_dividido:,.0f}")
    elif metodo2 == "Transferencia":
        # Escribir la segunda mitad en Transferencia
        context.app.revisar_pedido_page.escribir_numero_transferencia(f"${valor_dividido:,.0f}")
    else:
        raise ValueError(f"No se encontró el método de pago '{metodo2}'")
