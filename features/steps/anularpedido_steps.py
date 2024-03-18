# -*- coding: utf-8 -*-

from behave import given, when, then


@when('ingreso el correo electrónico "{correoElectronico}"')
def ingresar_correo(context, correoElectronico):
    context.app.login_page.ingresar_correo(correoElectronico)


@when('ingreso la contraseña "{contraseña}"')
def ingresar_contraseña(context, contraseña):
    context.app.login_page.ingresar_contraseña(contraseña)


@when('hago clic en el botón "Ingresar"')
def hacer_clic_ingresar(context):
    context.app.login_page.hacer_clic_ingresar()


@when('visualizo la factura con número "{numeroFactura}"')
def visualizar_factura(context, numeroFactura):
    context.app.invoice_page.visualizar_factura(numeroFactura)


@when('hago clic en el botón "Anular pedido"')
def clic_anular_pedido(context):
    context.app.invoice_page.clic_anular_pedido()


@then('valido que se haya abierto la pantalla de selección de motivo de anulación')
def validar_pantalla_anulacion(context):
    assert context.app.cancellation_reason_page.is_open()


@when('visualizo la pantalla de selección de motivo de anulación')
def visualizar_pantalla_anulacion(context):
    context.app.cancellation_reason_page.visualizar_pantalla_anulacion()


@then('valido la presencia de los siguientes motivos:')
def validar_presencia_motivos(context):
    for motivo in context.table:
        assert context.app.cancellation_reason_page.is_reason_present(motivo['Motivo'])


@then('valido la presencia del botón "Enviar motivo"')
def validar_presencia_boton_enviar(context):
    assert context.app.cancellation_reason_page.is_send_reason_button_present()


@when('hago clic en el botón "Enviar motivo"')
def clic_enviar_motivo(context):
    context.app.cancellation_reason_page.clic_enviar_motivo()


@then('verifico que se envíe el motivo seleccionado correctamente')
def verificar_envio_motivo(context):
    assert context.app.cancellation_reason_page.verificar_envio_motivo()


@when('elijo el nombre "{nombre}"')
def seleccionar_nombre(context, nombre):
    context.app.route_selection_page.seleccionar_nombre(nombre)


@when('hago clic en el botón "Anulados" en el sector de selección de rutas')
def clic_anulados(context):
    context.app.route_selection_page.clic_anulados()


@then('valido que la ruta utilizada anteriormente "{idRuta}" esté presente')
def validar_ruta_presente(context, idRuta):
    assert context.app.cancelled_orders_page.is_previous_route_present(idRuta)


@then('valido la presencia del texto "Sobre stock"')
def validar_texto_sobre_stock(context):
    assert context.app.cancelled_orders_page.is_text_present("Sobre stock")


@then('valido la presencia del botón "Comenzar ruta"')
def validar_presencia_boton_comenzar_ruta(context):
    assert context.app.cancelled_orders_page.is_start_route_button_present()


@when('visualizo la pantalla de retomar pedidos')
def visualizar_pantalla_retomar_pedidos(context):
    context.app.return_orders_page.visualizar_pantalla_retomar_pedidos()


@then('valido que la ruta del pedido sea "{ruta}"')
def validar_ruta_pedido(context, ruta):
    assert context.app.return_orders_page.validar_ruta_pedido(ruta)


@then('valido la presencia del botón "Retomar pedido"')
def validar_presencia_boton_retomar_pedido(context):
    assert context.app.return_orders_page.validar_presencia_boton_retomar_pedido()


@when('hago clic en el botón "Retomar pedido"')
def clic_retomar_pedido(context):
    context.app.return_orders_page.clic_retomar_pedido()


@then('verifico que se redireccione a la pantalla de detalles del pedido')
def verificar_redireccion_detalles(context):
    assert context.app.order_details_page.verificar_redireccion_detalles()


@then('verifico que se muestre correctamente el pedido a retomar')
def verificar_pedido_retomar(context):
    assert context.app.order_details_page.verificar_pedido_retomar()


@then('valido la presencia del botón "Ver detalle"')
def validar_presencia_boton_ver_detalle(context):
    assert context.app.return_orders_page.validar_presencia_boton_ver_detalle()


@when('hago clic en el botón "Ver detalle"')
def clic_ver_detalle(context):
    context.app.return_orders_page.clic_ver_detalle()


@then('verifico que se redireccione')
def verificar_redireccion(context):
    assert context.app.redirect_page.verificar_redireccion()
