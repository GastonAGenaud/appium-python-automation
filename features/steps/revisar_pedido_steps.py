from behave import given, when, then


@when('elijo la ruta "{idRuta}"')
def usuario_ingresa_correo(context, idRuta):
    if idRuta == "Avenida Las Condes":
        context.app.revisar_pedido_page.click_avenida_las_condes_btn()
    elif idRuta == "Pudahuel":
        context.app.revisar_pedido_page.click_pudahuel_btn()
    elif idRuta == "Renca":
        context.app.revisar_pedido_page.click_pudahuel_btn()
    else:
        raise ValueError(f"No se encontro la ruta '{idRuta}'")


@then('se valida que la visualizacion de pedido para la ruta "{idRuta}" sea correcta')
def visualizaciones_correcta_del_pedido(context, idRuta):
    if idRuta == "Avenida Las Condes":
        assert bool(context.app.revisar_pedido_page.valido_pedido_avenida_las_condes())
    elif idRuta == "Pudahuel":
        assert bool(context.app.revisar_pedido_page.valido_mensaje_error_contrasena())
    else:
        raise ValueError(f"No se encontro el mensaje de error en el campo de '{idRuta}'")


@then('valido la visualizacion del monto de la transferencia "{precio}" y de los productos "{producto}"')
def valido_monto_de_transferencia_y_productos(context, precio, producto):
    assert bool(context.app.revisar_pedido_page.valido_precio_del_pedido(precio))
    assert bool(context.app.revisar_pedido_page.valido_cantidad_de_productos(producto))


@then('valido la presencia de la opcion "{maps}"')
def valido_google_maps(context, maps):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps())


@when('visualizo la factura con numero "{factura}"')
def visualizo_la_factura(context, factura):
    assert bool(context.app.revisar_pedido_page.valido_numero_de_factura(factura))


@when('selecciono la factura con numero "{factura}"')
def visualizo_la_factura(context, factura):
    context.app.revisar_pedido_page.selecciono_la_factura(factura)


@then('valido que se muestre una confirmacion de anulacion del pedido')
def valido_anulacion_del_pedido(context):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps())


@then('valido que se muestre una confirmacion de entrega del pedido')
def valido_entrega_del_pedido(context):
    assert bool(context.app.revisar_pedido_page.valido_opcion_google_maps())


@then('valido el producto "{producto}"')
def valido_producto(context, producto):
    assert bool(context.app.revisar_pedido_page.valido_producto_coca_zero())


@then('valido el precio unitario "{precio}"')
def valido_precio_unitario(context, precio):
    assert bool(context.app.revisar_pedido_page.valido_precio_unitario())


@then('valido el sector de botones de agregar y restar')
def valido_sector_agregar_y_restar(context):
    assert bool(context.app.revisar_pedido_page.valido_restar_btn())
    assert bool(context.app.revisar_pedido_page.valido_agregar_btn())


@then('valido el precio final "{precio}"')
def valido_precio_final(context, precio):
    assert bool(context.app.revisar_pedido_page.valido_precio_final())


@then('valido que el precio total sea de "{precio}"')
def valido_total_precio(context, precio):
    assert bool(context.app.revisar_pedido_page.valido_precio_total())

