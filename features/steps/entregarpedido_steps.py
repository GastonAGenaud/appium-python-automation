from behave import given, when, then


@when('hago clic en el botón "Ingresar"')
def hacer_clic_ingresar(context):
    context.app.login_page.hacer_clic_ingresar()


@when('elijo la ruta "{nombreRuta}"')
def elegir_ruta(context, nombreRuta):
    context.app.entregar_pedido_page.seleccionar_ruta(nombreRuta)


@when('selecciono el botón "Comenzar ruta"')
def seleccionar_comenzar_ruta(context):
    context.app.entregar_pedido_page.hacer_clic_comenzar_ruta()


@when('visualizo la pantalla "Entregar pedidos" en el sector "Rebajados" con la factura "{numeroFactura}"')
def visualizar_pantalla_rebajados(context, numeroFactura):
    totalFactura = context.table[0]['totalFactura']
    totalRebajado = context.table[0]['totalRebajado']
    context.app.entregar_pedido_page.validar_pantalla_rebajados(numeroFactura, totalFactura, totalRebajado)


@when('visualizo la pantalla "Entregar pedidos" en el sector "Entregados" con la factura "{numeroFactura}"')
def visualizar_pantalla_entregados(context, numeroFactura):
    totalFactura = context.table[0]['totalFactura']
    totalRebajado = context.table[0]['totalRebajado']
    context.app.entregar_pedido_page.validar_pantalla_entregados(numeroFactura, totalFactura, totalRebajado)


@then('valido que el producto "{nombreProducto}" esté presente')
def validar_producto_presente(context, nombreProducto):
    context.app.entregar_pedido_page.validar_producto_presente(nombreProducto)


@then('valido el total de la factura como "{totalFactura}"')
def validar_total_factura(context, totalFactura):
    context.app.entregar_pedido_page.validar_total(totalFactura)


@then('valido el total rebajado como "{totalRebajado}"')
def validar_total_rebajado(context, totalRebajado):
    context.app.entregar_pedido_page.validar_total_rebajado(totalRebajado)


@then('valido la presencia del botón "Confirmar"')
def validar_presencia_boton_confirmar(context):
    context.app.entregar_pedido_page.validar_presencia_boton_confirmar()


@when('selecciono el botón "Confirmar"')
def seleccionar_boton_confirmar(context):
    context.app.entregar_pedido_page.confirmar_entrega()


@then('verifico que al confirmar se redirija a la pantalla de confirmación de entrega')
def verificar_redireccion_confirmacion(context):
    context.app.entregar_pedido_page.verificar_redireccion_confirmacion()
