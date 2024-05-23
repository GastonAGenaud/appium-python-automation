from behave import given, when, then


@when('elijo la ruta "{idRuta}"')
def usuario_ingresa_correo(context, idRuta):
    if idRuta == "Avenida Las Condes":
        context.app.revisar_pedido_page.click_avenida_las_condes_btn()
    elif idRuta == "Pudahuel":
        context.app.revisar_pedido_page.click_pudahuel_btn()
    elif idRuta == "Renca":
        context.app.revisar_pedido_page.click_renca_btn()
    elif idRuta == "El Deseo SPA":
        context.app.revisar_pedido_page.click_el_deseo_spa_btn()
    else:
        raise ValueError(f"No se encontro la ruta '{idRuta}'")


@then('se valida que la visualizacion de pedido para la ruta "{idRuta}" sea correcta')
def visualizaciones_correcta_del_pedido(context, idRuta):
    if idRuta == "Avenida Las Condes":
        assert bool(context.app.revisar_pedido_page.valido_pedido_avenida_las_condes())
    elif idRuta == "Pudahuel":
        assert bool(context.app.revisar_pedido_page.valido_pedido_pudahuel())
    elif idRuta == "Renca":
        assert bool(context.app.revisar_pedido_page.valido_pedido_renca())
    elif idRuta == "El Deseo SPA":
        assert bool(context.app.revisar_pedido_page.valido_pedido_el_deseo_spa())
    else:
        raise ValueError(f"No se encontro el mensaje de error en el campo de '{idRuta}'")


@then('valido la visualizacion del monto de la transferencia')
def valido_visualizacion_de_transferencia(context):
    assert bool(context.app.revisar_pedido_page.valido_precio_del_pedido())


@then('valido la visualizacion de la cantidad de los productos')
def valido_visualizacion_de_cantidad(context):
    assert bool(context.app.revisar_pedido_page.valido_cantidad_de_productos())


@then('valido la presencia de la opcion "{maps}"')
def valido_google_maps(context, maps):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps())


@when('visualizo la factura con numero "{factura}"')
def visualizo_la_factura(context, factura):
    assert bool(context.app.revisar_pedido_page.valido_numero_de_factura(factura))


@when('selecciono la factura con numero "{factura}"')
def visualizo_la_factura(context, factura):
    if factura == "388717884":
        context.app.revisar_pedido_page.selecciono_la_factura()
    elif factura == "404145544":
        context.app.revisar_pedido_page.selecciono_la_factura_deseo_spa()
    else:
        raise ValueError(f"No se encontro la factura con numero '{factura}'")


@then('valido que se muestre una confirmacion de anulacion del pedido')
def valido_anulacion_del_pedido(context):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps())


@then('valido el producto "{producto}"')
def valido_producto(context, producto):
    if producto == "Coca Cola LT220cc":
        assert bool(context.app.revisar_pedido_page.valido_producto_coca_cola())
    elif producto == "Fanta MidCal PT250cc":
        assert bool(context.app.revisar_pedido_page.valido_producto_fanta())
    elif producto == "Fanta MidCal Express 237cc":
        assert bool(context.app.revisar_pedido_page.valido_producto_fanta_express())
    else:
        raise ValueError(f"No se encontro el producto '{producto}'")


@then('valido el precio unitario "{precio}"')
def valido_precio_unitario(context, precio):
    if precio == "$ 57.652":
        assert bool(context.app.revisar_pedido_page.valido_precio_unitario_coca_cola())
    elif precio == "$ 46.913":
        assert bool(context.app.revisar_pedido_page.valido_precio_unitario_fanta())
    elif precio == "$ 66.471":
        assert bool(context.app.revisar_pedido_page.valido_precio_unitario_fanta_express())
    else:
        raise ValueError(f"No se encontro el precio '{precio}'")


@then('valido la cantidad de pack pedidos "{cantidad}"')
def valido_cantidad_pack(context, cantidad):
    if cantidad == "4":
        assert bool(context.app.revisar_pedido_page.valido_cantidad_pack_coca_cola())
    elif cantidad == "5":
        assert bool(context.app.revisar_pedido_page.valido_cantidad_pack_fanta())
    elif cantidad == "7":
        assert bool(context.app.revisar_pedido_page.valido_cantidad_pack_fanta_express())
    else:
        raise ValueError(f"No se encontro la cantidad de pack pedidos '{cantidad}'")


@then('valido el sector de botones de agregar y restar')
def valido_sector_agregar_y_restar(context):
    assert bool(context.app.revisar_pedido_page.valido_restar_btn())
    assert bool(context.app.revisar_pedido_page.valido_agregar_btn())


@when('selecciono el botón de restar producto')
def valido_sector_agregar_y_restar(context):
    assert bool(context.app.revisar_pedido_page.valido_restar_btn())


@then('valido el precio final "{precio}"')
def valido_precio_final(context, precio):
    if precio == "$ 230.608":
        assert bool(context.app.revisar_pedido_page.valido_precio_final_coca_cola())
    elif precio == "$ 234.565":
        assert bool(context.app.revisar_pedido_page.valido_precio_final_fanta())
    elif precio == "$ 465.297":
        assert bool(context.app.revisar_pedido_page.valido_precio_final_fanta_express())
    else:
        raise ValueError(f"No se encontro la cantidad de pack pedidos '{precio}'")


@then('valido que el precio total sea de "{precio}"')
def valido_total_precio(context, precio):
    assert bool(context.app.revisar_pedido_page.valido_precio_total())


@then('valido que este correcta la suma del precio de los productos')
def valido_sea_correcto_precio(context):
    assert bool(context.app.revisar_pedido_page.valido_comparacion_de_precio())

