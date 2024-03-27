from behave import given, when, then

<<<<<<< HEAD
=======

@when('visualizo la factura con número "{numeroFactura}"')
def visualizar_factura(context, numeroFactura):
    return True


@when('hago clic en el botón "Anular pedido"')
def clic_anular_pedido(context):
    return True


@then('valido que se haya abierto la pantalla de selección de motivo de anulación')
def validar_pantalla_anulacion(context):
    return True


@when('visualizo la pantalla de selección de motivo de anulación')
def visualizar_pantalla_anulacion(context):
    return True


@then('valido la presencia de los siguientes motivos:')
def validar_presencia_motivos(context):
    return True


@then('valido la presencia del botón "Enviar motivo"')
def validar_presencia_boton_enviar(context):
    return True


@when('hago clic en el botón "Enviar motivo"')
def clic_enviar_motivo(context):
    return True


@when('elijo el nombre "{nombre}"')
def seleccionar_nombre(context, nombre):
    return True


@when('hago clic en el botón "Anulados" en el sector de selección de rutas')
def clic_anulados(context):
    return True


@then('valido que la ruta utilizada anteriormente "{idRuta}" esté presente')
def validar_ruta_presente(context, idRuta):
    return True


@then('valido la presencia del texto "Sobre stock"')
def validar_texto_sobre_stock(context):
    return True


@then('valido la presencia del botón "Comenzar ruta"')
def validar_presencia_boton_comenzar_ruta(context):
    return True


@when('visualizo la pantalla de retomar pedidos')
def visualizar_pantalla_retomar_pedidos(context):
    return True


@then('valido que la ruta del pedido sea "{ruta}"')
def validar_ruta_pedido(context, ruta):
    return True


@then('valido la presencia del botón "Retomar pedido"')
def validar_presencia_boton_retomar_pedido(context):
    return True


@when('hago clic en el botón "Retomar pedido"')
def clic_retomar_pedido(context):
    return True


@then('verifico que se redireccione a la pantalla de detalles del pedido')
def verificar_redireccion_detalles(context):
    return True


@then('verifico que se muestre correctamente el pedido a retomar')
def verificar_pedido_retomar(context):
    return True


@then('valido la presencia del botón "Ver detalle"')
def validar_presencia_boton_ver_detalle(context):
    return True


@when('hago clic en el botón "Ver detalle"')
def clic_ver_detalle(context):
    return True


@then('verifico que se redireccione')
def verificar_redireccion(context):
    return True
>>>>>>> a95637b251ca4f3486cd0ac963c2aed92ef642c5
