from behave import given, when, then


@when('hago clic en el botón "Ingresar"')
def hacer_clic_ingresar(context):
    context.page_object.hacer_clic_ingresar()


@when('elijo la ruta "{nombreRuta}"')
def elegir_ruta(context, nombreRuta):
    context.page_object.elegir_ruta(nombreRuta)


@when('selecciono el botón "Comenzar ruta"')
def seleccionar_comenzar_ruta(context):
    context.page_object.seleccionar_comenzar_ruta()


@when('visualizo la pantalla "Entregar pedidos" en el sector "Rebajados" con la factura "{numeroFactura}"')
def visualizar_pantalla_rebajados(context, numeroFactura):
    context.page_object.visualizar_pantalla_rebajados(numeroFactura)


@when('visualizo la pantalla "Entregar pedidos" en el sector "Entregados" con la factura "{numeroFactura}"')
def visualizar_pantalla_entregados(context, numeroFactura):
    context.page_object.visualizar_pantalla_entregados(numeroFactura)


@then('valido que el producto "{nombreProducto}" esté presente')
def validar_producto_presente(context, nombreProducto):
    context.page_object.validar_producto_presente(nombreProducto)


@then('valido el total de la factura como "{totalFactura}"')
def validar_total_factura(context, totalFactura):
    context.page_object.validar_total_factura(totalFactura)


@then('valido el total rebajado como "{totalRebajado}"')
def validar_total_rebajado(context, totalRebajado):
    context.page_object.validar_total_rebajado(totalRebajado)


@then('valido la presencia del botón "Confirmar"')
def validar_presencia_boton_confirmar(context):
    context.page_object.validar_presencia_boton_confirmar()


@when('selecciono el botón "Confirmar"')
def seleccionar_boton_confirmar(context):
    context.page_object.seleccionar_boton_confirmar()


@then('verifico que al confirmar se redirija a la pantalla de confirmación de entrega')
def verificar_redireccion_confirmacion(context):
    context.page_object.verificar_redireccion_confirmacion()
