from behave import given, when, then


@when('elijo la ruta "{idRuta}"')
def usuario_elije_ruta(context, idRuta):
    if idRuta == "El Deseo SPA":
        context.app.ux_page.click_el_deseo_spa_btn()
    elif idRuta == "LIKE EAT FOODS SPA":
        context.app.revisar_pedido_page.click_like_eat_foods_spa_btn()
    else:
        raise ValueError(f"No se encontró la ruta '{idRuta}'")


@then('se valida que la visualizacion de pedido para la ruta "{idRuta}" sea correcta')
def visualizaciones_correcta_del_pedido(context, idRuta):
    assert bool(
        context.app.revisar_pedido_page.valido_pedido_el_deseo_spa()), f"Visualización incorrecta para la ruta '{idRuta}'"


@then('valido la visualizacion del monto de la transferencia')
def valido_visualizacion_de_transferencia(context):
    assert bool(
        context.app.revisar_pedido_page.valido_precio_del_pedido()), "El monto de la transferencia no es visible"


@then('valido la visualizacion de la cantidad de los productos')
def valido_visualizacion_de_cantidad(context):
    assert bool(
        context.app.revisar_pedido_page.valido_cantidad_de_productos()), "La cantidad de productos no es visible"


@then('valido la presencia de la opcion "{maps}"')
def valido_google_maps(context, maps):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps()), f"La opción '{maps}' no está presente"


@when('selecciono la factura con numero "{factura}"')
def visualizo_la_factura(context, factura):
    if factura == "404145531":
        context.app.revisar_pedido_page.selecciono_la_factura()
    elif factura == "404145535":
        context.app.revisar_pedido_page.selecciono_la_factura_foods_spa()
    elif factura == "83908330":
        context.app.revisar_pedido_page.selecciono_la_factura_erbi_A()
    elif factura == "8390812":
        context.app.revisar_pedido_page.selecciono_la_factura_erbi_B()
    else:
        raise ValueError(f"No se encontró la factura con número '{factura}'")


@when('selecciono la segunda factura con numero "{factura}"')
def visualizo_la_factura2(context, factura):
    if factura == "404145531":
        context.app.revisar_pedido_page.selecciono_la_factura2()
    elif factura == "404145535":
        context.app.revisar_pedido_page.selecciono_la_factura_foods_spa2()
    else:
        raise ValueError(f"No se encontró la segunda factura con número '{factura}'")


@then('valido que se muestre una confirmacion de anulacion del pedido')
def valido_anulacion_del_pedido(context):
    assert bool(
        context.app.revisar_pedido_page.valido_opcion_google_maps()), ("La confirmación de anulación del pedido no es "
                                                                       "visible")


@then('valido el producto "{producto}"')
def valido_producto(context, producto):
    if producto == "Sprite MidCal PT250cc x6":
        assert bool(
            context.app.revisar_pedido_page.valido_producto_sprite_MidCal()), (f"El producto '{producto}' no está en "
                                                                               f"la lista")
    elif producto == "Fanta MidCal Express 237cc x 24":
        assert bool(
            context.app.revisar_pedido_page.valido_producto_fanta_express()), (f"El producto '{producto}' no está en "
                                                                               f"la lista")
    elif producto == "Benedictino S/G PT6.5 x 2 Cilindrico":
        assert bool(
            context.app.revisar_pedido_page.benedictino_cilindrico_pedido()), (f"El producto '{producto}' no está en "
                                                                               f"la lista")
    else:
        raise ValueError(f"No se encontró el producto '{producto}'")


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


@then('valido el sector de botones de agregar y restar')
def valido_sector_agregar_y_restar(context):
    assert bool(context.app.revisar_pedido_page.valido_restar_btn()), "El botón de restar no está visible"
    assert bool(context.app.revisar_pedido_page.valido_agregar_btn()), "El botón de agregar no está visible"


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


@then('valido que el precio total sea de "{precio}"')
def valido_total_precio(context, precio):
    assert bool(context.app.revisar_pedido_page.valido_precio_total()), f"El precio total '{precio}' no es correcto"


@then('valido que este correcta la suma del precio de los productos')
def valido_sea_correcto_precio(context):
    assert bool(
        context.app.revisar_pedido_page.valido_comparacion_de_precio()), ("La suma del precio de los productos no es "
                                                                          "correcta")


@then('valido que la nota de credito sea "{monto}"')
def valido_nota_de_credito(context, monto):
    assert bool(context.app.revisar_pedido_page.valido_nota_pedido()), f"La nota de crédito '{monto}' no es correcta"


@when('hago click en la opcion "{metodo}"')
def hago_click_opcion_metodo(context, metodo):
    context.app.revisar_pedido_page.click_metodo_de_pago()


@when('selecciono el metodo de pago "{metodo}"')
def selecciono_metodo_de_pago(context, metodo):
    if metodo == "Transferencia":
        context.app.revisar_pedido_page.click_transferencia_opcion()
    elif metodo == "Efectivo":
        context.app.revisar_pedido_page.click_efectivo_opcion()
    elif metodo == "Con más de un método de pago":
        context.app.revisar_pedido_page.mas_de_un_metodo()
    else:
        raise ValueError(f"No se encontró el método de pago '{metodo}'")


@then('valido que sea visible el metodo de pago "{metodo}"')
def valido_sea_visible_metodo(context, metodo):
    if metodo == "Transferencia":
        assert bool(
            context.app.revisar_pedido_page.valido_transferencia_opcion()), f"El método de pago '{metodo}' no está visible"
    elif metodo == "Efectivo":
        assert bool(
            context.app.revisar_pedido_page.valido_efectivo_opcion()), f"El método de pago '{metodo}' no está visible"
    elif metodo == "Con más de un método de pago":
        assert bool(
            context.app.revisar_pedido_page.valido_mas_de_un_metodo_opcion()), f"El método de pago '{metodo}' no está visible"
    else:
        raise ValueError(f"No se encontró el método de pago '{metodo}'")


@then('valido que el metodo de pago fue seleccionado')
def valido_sea_seleccionado_metodo(context):
    assert bool(context.app.revisar_pedido_page.valido_metodo_seleccionado()), "El método de pago no fue seleccionado"


@then('valido el mensaje "Metodo de pago editado"')
def valido_mensaje_pago_editado(context):
    assert bool(
        context.app.revisar_pedido_page.metodo_pago_mensaje()), "El mensaje 'Método de pago editado' no es visible"


@then('valido el mensaje que se muestra en el sector Cheque')
def valido_mensaje_sector_cheque(context):
    assert bool(
        context.app.revisar_pedido_page.cheque_mensaje_no_poder_usar()), "El mensaje que se muestra en el sector Cheque"


@when('hago click en el check "{metodo}"')
def valido_check_como_pagar(context, metodo):
    if metodo == "Efectivo":
        context.app.revisar_pedido_page.seleccionar_check_efectivo()
    elif metodo == "Transferencia":
        context.app.revisar_pedido_page.seleccionar_check_transferencia()
    else:
        raise ValueError(f"No se encontró el check de '{metodo}'")


@when('Ingreso los montos en efectivo y transferencia')
def ingreso_montos_efectivo_transferencia(context):
    context.app.revisar_pedido_page.ingreso_montos_transferencia_efectivo()


@when('selecciono la vuelta "{vuelta}"')
def seleccionar_vuelta(context, vuelta):
    context.app.revisar_pedido_page.click_vuelta_1()


@then("valido el numero de telefono del local")
def valido_numero_telefono(context):
    assert context.app.revisar_pedido_page.numero_telefono_local_visible(), \
        "El número de teléfono del local no está visible en la pantalla"


@then("valido el horario del cierre del local")
def valido_horario_cierre(context):
    assert context.app.revisar_pedido_page.cierre_de_local(), "El mensaje que se muestra en el sector horario no es válido"


