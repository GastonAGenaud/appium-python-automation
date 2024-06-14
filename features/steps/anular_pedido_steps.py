from behave import given, when, then


@when('selecciono el boton "Retornar pedido"')
def selecciono_retornar_pedido(context):
    context.app.anular_pedido_page.selecciono_retornar_pedido()


@then('valido la presencia de los siguientes motivos')
def validar_presencia_motivos(context):
    motivos = [row['motivo'] for row in context.table]
    assert context.app.anular_pedido_page.valido_pantalla_motivo_anulacion()


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
