from behave import given, when, then


@when('visualizo la factura con número "{numeroFactura}"')
def visualizar_factura(context, numeroFactura):
    assert bool(context.app.revisar_pedido_page.valido_numero_de_factura(numeroFactura))


@when('hago clic en el botón "Anular pedido"')
def clic_anular_pedido(context):
    context.app.anular_pedido_page.click_anular_pedido_btn()


@then('valido que se haya abierto la pantalla de selección de motivo de anulación')
def validar_pantalla_anulacion(context):
    assert bool(context.app.anular_pedido_page.valido_pantalla_motivo_anulacion())


@when('visualizo la pantalla de selección de motivo de anulación')
def visualizar_pantalla_anulacion(context):
    assert bool(context.app.anular_pedido_page.valido_pantalla_motivo_anulacion())


@then('valido la presencia de los siguientes motivos:')
def validar_presencia_motivos(context):
    assert bool(context.app.anular_pedido_page.valido_motivos_anulacion())


@then('valido la presencia del botón "Enviar motivo"')
def validar_presencia_boton_enviar(context):
    assert bool(context.app.anular_pedido_page.valido_boton_enviar_motivo())


@when('hago clic en el botón "Enviar motivo"')
def clic_enviar_motivo(context):
    context.app.anular_pedido_page.click_enviar_motivo_btn()


@when('elijo el nombre "{nombre}"')
def seleccionar_nombre(context, nombre):
    context.app.anular_pedido_page.seleccionar_nombre(nombre)


@when('hago clic en el botón "Anulados" en el sector de selección de rutas')
def clic_anulados(context):
    context.app.anular_pedido_page.click_anulados_btn()


@then('valido que la ruta utilizada anteriormente "{idRuta}" esté presente')
def validar_ruta_presente(context, idRuta):
    assert bool(context.app.anular_pedido_page.valido_ruta_presente(idRuta))


@then('valido la presencia del texto "Sobre stock"')
def validar_texto_sobre_stock(context):
    assert bool(context.app.anular_pedido_page.valido_texto_sobre_stock())


@then('valido la presencia del botón "Comenzar ruta"')
def validar_presencia_boton_comenzar_ruta(context):
    assert bool(context.app.anular_pedido_page.valido_boton_comenzar_ruta())


@when('visualizo la pantalla de retomar pedidos')
def visualizar_pantalla_retomar_pedidos(context):
    assert bool(context.app.anular_pedido_page.valido_pantalla_retomar_pedidos())


@then('valido que la ruta del pedido sea "{ruta}"')
def validar_ruta_pedido(context, ruta):
    assert bool(context.app.anular_pedido_page.valido_ruta_pedido(ruta))


@then('valido la presencia del botón "Retomar pedido"')
def validar_presencia_boton_retomar_pedido(context):
    assert bool(context.app.anular_pedido_page.valido_boton_retomar_pedido())


@when('hago clic en el botón "Retomar pedido"')
def clic_retomar_pedido(context):
    context.app.anular_pedido_page.click_retomar_pedido_btn()


@then('verifico que se redireccione a la pantalla de detalles del pedido')
def verificar_redireccion_detalles(context):
    assert bool(context.app.anular_pedido_page.valido_redireccion_detalles())


@then('verifico que se muestre correctamente el pedido a retomar')
def verificar_pedido_retomar(context):
    assert bool(context.app.anular_pedido_page.valido_pedido_retomar())


@then('valido la presencia del botón "Ver detalle"')
def validar_presencia_boton_ver_detalle(context):
    assert bool(context.app.anular_pedido_page.valido_boton_ver_detalle())


@when('hago clic en el botón "Ver detalle"')
def clic_ver_detalle(context):
    context.app.anular_pedido_page.click_ver_detalle_btn()


@then('verifico que se redireccione')
def verificar_redireccion(context):
    assert bool(context.app.anular_pedido_page.valido_redireccion())
