from behave import given, when, then


@when('selecciono el boton "Retornar pedido"')
def selecciono_retornar_pedido(context):
    context.app.anular_pedido_page.selecciono_retornar_pedido()


@then('valido la presencia de los siguientes motivos')
def validar_presencia_motivos(context):
    motivos = [row['motivo'] for row in context.table]
    assert context.app.anular_pedido_page.valido_pantalla_motivo_anulacion()


@then('selecciono "Sobre stock"')
def seleccionar_motivo(context):
    context.app.anular_pedido_page.seleccionar_nombre("Sobre stock")


@when('selecciono "Sobre stock"')
def seleccionar_motivo(context):
    context.app.anular_pedido_page.seleccionar_nombre("Sobre stock")


@then('valido la presencia del botón "Confirmar"')
def validar_presencia_boton_confirmar(context):
    assert context.app.anular_pedido_page.valido_boton_enviar_motivo()


@when('hago clic en el botón "Confirmar"')
def clic_confirmar(context):
    context.app.anular_pedido_page.click_confirmar_btn()


@when('hago clic en el botón "Retornados"')
def clic_retornados(context):
    context.app.anular_pedido_page.selecciono_boton_retornado()


@then('verifico que se redireccione a la pantalla de detalles del pedido')
def validar_pantalla_retomar_detalles(context):
    context.app.anular_pedido_page.valido_pantalla_retomar_detalles()


@when('verifico que se muestre correctamente el pedido a retomar')
def validar_retomar(context):
    context.app.anular_pedido_page.validar_retomar()


@then('Valido la pantalla de retomar pedidos')
def pantalla_retomar_pedidos(context):
    context.app.anular_pedido_page.valido_pantalla_retomar()


@then('valido que la ruta utilizada anteriormente esté presente')
def deseo_spa_retornados(context):
    assert context.app.anular_pedido_page.deseo_spa_retornados(), (
        "La ruta 'El Deseo SPA' no está presente en el sector 'Retornados'.")


@then('verifico que se envíe el motivo seleccionado correctamente')
def verificar_envio_motivo(context):
    assert context.app.anular_pedido_page.valido_cliente_retornado_mensaje()


@then('verifico la validacion del retorno de la factura')
def valido_boton_ver_detalle(context):
    assert context.app.anular_pedido_page.valido_texto_porque_retornar()


@then('valido que se haya abierto la pantalla de selección de motivo de anulación')
def valido_texto_porque_retornar(context):
    assert context.app.anular_pedido_page.valido_boton_ver_detalle()


@when('visualizo la pantalla de selección de motivo de anulacion')
def valido_redireccion_detalles(context):
    assert context.app.anular_pedido_page.valido_pantalla_motivo_anulacion()
