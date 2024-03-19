from behave import given, when, then


@when('hago clic en el botón "Ingresar"')
def hacer_clic_ingresar(context):
    return True


@when('elijo la ruta "{nombreRuta}"')
def elegir_ruta(context, nombreRuta):
    return True


@when('selecciono el botón "Comenzar ruta"')
def seleccionar_comenzar_ruta(context):
    return True


@when('visualizo la pantalla "Entregar pedidos" en el sector "Rebajados" con la factura "{numeroFactura}"')
def visualizar_pantalla_rebajados(context, numeroFactura):
    return True


@when('visualizo la pantalla "Entregar pedidos" en el sector "Entregados" con la factura "{numeroFactura}"')
def visualizar_pantalla_entregados(context, numeroFactura):
    return True


@then('valido que el producto "{nombreProducto}" esté presente')
def validar_producto_presente(context, nombreProducto):
    return True


@then('valido el total de la factura como "{totalFactura}"')
def validar_total_factura(context, totalFactura):
    return True


@then('valido el total rebajado como "{totalRebajado}"')
def validar_total_rebajado(context, totalRebajado):
    return True


@then('valido la presencia del botón "Confirmar"')
def validar_presencia_boton_confirmar(context):
    return True


@when('selecciono el botón "Confirmar"')
def seleccionar_boton_confirmar(context):
    return True


@then('verifico que al confirmar se redirija a la pantalla de confirmación de entrega')
def verificar_redireccion_confirmacion(context):
    return True
