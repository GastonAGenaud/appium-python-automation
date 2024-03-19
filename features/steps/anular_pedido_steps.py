from behave import given, when, then
from features.pages.anular_pedido_page import AnulacionPage


@when('visualizo la factura con número "{numeroFactura}"')
def visualizar_factura(context, numeroFactura):
    context.anulacion_page = AnulacionPage(context.driver)
    return context.anulacion_page.visualizar_factura(numeroFactura)


@when('hago clic en el botón "Anular pedido"')
def clic_anular_pedido(context):
    return context.anulacion_page.clic_anular_pedido()


@then('valido que se haya abierto la pantalla de selección de motivo de anulación')
def validar_pantalla_anulacion(context):
    return context.anulacion_page.validar_pantalla_anulacion()


@when('visualizo la pantalla de selección de motivo de anulación')
def visualizar_pantalla_anulacion(context):
    return context.anulacion_page.visualizar_pantalla_anulacion()


@then('valido la presencia de los siguientes motivos:')
def validar_presencia_motivos(context):
    return context.anulacion_page.validar_presencia_motivos()


@then('valido la presencia del botón "Enviar motivo"')
def validar_presencia_boton_enviar(context):
    return context.anulacion_page.validar_presencia_boton_enviar()


@when('hago clic en el botón "Enviar motivo"')
def clic_enviar_motivo(context):
    return context.anulacion_page.clic_enviar_motivo()


@when('elijo el nombre "{nombre}"')
def seleccionar_nombre(context, nombre):
    return context.anulacion_page.seleccionar_nombre(nombre)


@when('hago clic en el botón "Anulados" en el sector de selección de rutas')
def clic_anulados(context):
    return context.anulacion_page.clic_anulados()


@then('valido que la ruta utilizada anteriormente "{idRuta}" esté presente')
def validar_ruta_presente(context, idRuta):
    return context.anulacion_page.validar_ruta_presente(idRuta)


@then('valido la presencia del texto "Sobre stock"')
def validar_texto_sobre_stock(context):
    return context.anulacion_page.validar_texto_sobre_stock()


@then('valido la presencia del botón "Comenzar ruta"')
def validar_presencia_boton_comenzar_ruta(context):
    return context.anulacion_page.validar_presencia_boton_comenzar_ruta()


@when('visualizo la pantalla de retomar pedidos')
def visualizar_pantalla_retomar_pedidos(context):
    return context.anulacion_page.visualizar_pantalla_retomar_pedidos()


@then('valido que la ruta del pedido sea "{ruta}"')
def validar_ruta_pedido(context, ruta):
    return context.anulacion_page.validar_ruta_pedido(ruta)


@then('valido la presencia del botón "Retomar pedido"')
def validar_presencia_boton_retomar_pedido(context):
    return context.anulacion_page.validar_presencia_boton_retomar_pedido()


@when('hago clic en el botón "Retomar pedido"')
def clic_retomar_pedido(context):
    return context.anulacion_page.clic_retomar_pedido()


@then('verifico que se redireccione a la pantalla de detalles del pedido')
def verificar_redireccion_detalles(context):
    return context.anulacion_page.verificar_redireccion_detalles()


@then('verifico que se muestre correctamente el pedido a retomar')
def verificar_pedido_retomar(context):
    return context.anulacion_page.verificar_pedido_retomar()


@then('valido la presencia del botón "Ver detalle"')
def validar_presencia_boton_ver_detalle(context):
    return context.anulacion_page.validar_presencia_boton_ver_detalle()


@when('hago clic en el botón "Ver detalle"')
def clic_ver_detalle(context):
    return context.anulacion_page.clic_ver_detalle()


@then('verifico que se redireccione')
def verificar_redireccion(context):
    return context.anulacion_page.verificar_redireccion()
