from behave import given, when, then


@when('elijo la ruta "{idRuta}"')
def usuario_elije_ruta(context, idRuta):
    if idRuta == "El Deseo SPA":
        context.app.ux_page.click_el_deseo_spa_btn()
    elif idRuta == "Erbi":
        context.app.revisar_pedido_page.click_erbi_btn()
    else:
        raise ValueError(f"No se encontro la ruta '{idRuta}'")


@then('se valida que la visualizacion de pedido para la ruta "{idRuta}" sea correcta')
def visualizaciones_correcta_del_pedido(context, idRuta):
    assert bool(context.app.revisar_pedido_page.valido_pedido_el_deseo_spa())


@then('valido la visualizacion del monto de la transferencia')
def valido_visualizacion_de_transferencia(context):
    assert bool(context.app.revisar_pedido_page.valido_precio_del_pedido())


@then('valido la visualizacion de la cantidad de los productos')
def valido_visualizacion_de_cantidad(context):
    assert bool(context.app.revisar_pedido_page.valido_cantidad_de_productos())


@then('valido la presencia de la opcion "{maps}"')
def valido_google_maps(context, maps):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps())


@when('selecciono la factura con numero "{factura}"')
def visualizo_la_factura(context, factura):
    if factura == "404145531":
        context.app.revisar_pedido_page.selecciono_la_factura()
    elif factura == "83908330":
        context.app.revisar_pedido_page.selecciono_la_factura_erbi_A()
    elif factura == "8390812":
        context.app.revisar_pedido_page.selecciono_la_factura_erbi_B()
    else:
        raise ValueError(f"No se encontro la factura con numero '{factura}'")


@when('selecciono la segunda factura con numero "{factura}"')
def visualizo_la_factura2(context, factura):
    if factura == "404145531":
        context.app.revisar_pedido_page.selecciono_la_factura2()
    else:
        raise ValueError(f"No se encontro la factura con numero '{factura}'")


@then('valido que se muestre una confirmacion de anulacion del pedido')
def valido_anulacion_del_pedido(context):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps())


@then('valido el producto "{producto}"')
def valido_producto(context, producto):
    if producto == "Sprite MidCal PT250cc x6":
        assert bool(context.app.revisar_pedido_page.valido_producto_sprite_MidCal())
    elif producto == "Fanta MidCal Express 237cc x 24":
        assert bool(context.app.revisar_pedido_page.valido_producto_fanta_express())
    elif producto == "Benedictino S/G PT6.5 x 2 Cilindrico":
        assert bool(context.app.revisar_pedido_page.benedictino_cilindrico_pedido())
    else:
        raise ValueError(f"No se encontro el producto '{producto}'")


@then('valido el precio unitario "{precio}"')
def valido_precio_unitario(context, precio):
    if precio == "$65.064":
        assert bool(context.app.revisar_pedido_page.valido_precio_unitario_sprite_midCal())
    elif precio == "$66.210":
        assert bool(context.app.revisar_pedido_page.valido_precio_unitario_fanta())
    elif precio == "$376.873":
        assert bool(context.app.revisar_pedido_page.valido_precio_unitario_benedictino())
    else:
        raise ValueError(f"No se encontro el precio '{precio}'")


@then('valido el precio unitario "{precio}" en la factura')
def valido_precio_unitario_factura(context, precio):
    if precio == "$ 65.064":
        assert bool(context.app.revisar_pedido_page.valido_producto_sprite_express())
    elif precio == "$ 53.839":
        assert bool(context.app.revisar_pedido_page.valido_benedictino_precio_unitario())
    elif precio == "$ 33.105":
        assert bool(context.app.revisar_pedido_page.valido_fanta_MidCal_precio_unitario())
    else:
        raise ValueError(f"No se encontró el precio '{precio}' para validar en la factura")


@then('valido la cantidad de pack pedidos "{cantidad}"')
def valido_cantidad_pack(context, cantidad):
    if cantidad == "1":
        assert bool(context.app.revisar_pedido_page.valido_cantidad_pack_sprite_express())
    elif cantidad == "2":
        assert bool(context.app.revisar_pedido_page.valido_cantidad_pack_fanta())
    elif cantidad == "7":
        assert bool(context.app.revisar_pedido_page.valido_cantidad_pack_benedictino())
    else:
        raise ValueError(f"No se encontró la cantidad de pack pedidos '{cantidad}'")


@then('valido el sector de botones de agregar y restar')
def valido_sector_agregar_y_restar(context):
    assert bool(context.app.revisar_pedido_page.valido_restar_btn())
    assert bool(context.app.revisar_pedido_page.valido_agregar_btn())


@then('valido el precio final "{precio}"')
def valido_precio_final(context, precio):
    if precio == "$ 65.064":
        assert bool(context.app.revisar_pedido_page.valido_precio_final_sprite())
    elif precio == "$ 66.210":
        assert bool(context.app.revisar_pedido_page.valido_precio_final_fanta())
    elif precio == "$ 376.873":
        assert bool(context.app.revisar_pedido_page.valido_precio_final_benedictino())
    else:
        raise ValueError(f"No se encontro la cantidad de pack pedidos '{precio}'")


@then('valido que el precio total sea de "{precio}"')
def valido_total_precio(context, precio):
    assert bool(context.app.revisar_pedido_page.valido_precio_total())


@then('valido que este correcta la suma del precio de los productos')
def valido_sea_correcto_precio(context):
    assert bool(context.app.revisar_pedido_page.valido_comparacion_de_precio())


@then('valido que la nota de credito sea "{monto}"')
def valido_nota_de_credito(context, monto):
    assert bool(context.app.revisar_pedido_page.valido_nota_pedido())


@when('hago click en la opcion "{metodo}"')
def hago_click_opcion_metodo(context, metodo):
    context.app.revisar_pedido_page.click_metodo_de_pago()


@when('selecciono el metodo de pago "{metodo}"')
def selecciono_metodo_de_pago(context, metodo):
    if metodo == "Transferencia":
        context.app.revisar_pedido_page.click_transferencia_opcion()
    elif metodo == "Efectivo":
        context.app.revisar_pedido_page.click_efectivo_opcion()
    elif metodo == "Con mas de un metodo de pago":
        context.app.revisar_pedido_page.click_mas_de_un_metodo_opcion()
    else:
        raise ValueError(f"No se encontro el metodo de pago de '{metodo}'")


@then('valido que sea visible el metodo de de pago "{metodo}"')
def valido_sea_visible_metodo(context, metodo):
    if metodo == "Transferencia":
        assert bool(context.app.revisar_pedido_page.valido_transferencia_opcion())
    elif metodo == "Efectivo":
        assert bool(context.app.revisar_pedido_page.valido_efectivo_opcion())
    elif metodo == "Con mas de un metodo de pago":
        assert bool(context.app.revisar_pedido_page.valido_mas_de_un_metodo_opcion())
    else:
        raise ValueError(f"No se encontro el metodo de pago de '{metodo}'")


@then('valido que el metodo de pago fue seleccionado')
def valido_sea_seleccionado_metodo(context):
    assert bool(context.app.revisar_pedido_page.valido_metodo_seleccionado())
