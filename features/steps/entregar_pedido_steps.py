from behave import given, when, then


@when('selecciono para rebajar el pedido')
def rebajar_el_pedido(context):
    context.app.entregar_pedido_page.rebajo_el_pedido()


@then('valido el total de la factura como "{precio}"')
def valido_el_total_de_factura(context, precio):
    assert bool(context.app.entregar_pedido_page.valido_precio_total_factura())


@then('valido el total rebajado como "{precio}"')
def valido_el_total_rebajado(context, precio):
    assert bool(context.app.entregar_pedido_page.valido_precio_rebajado())


@then('valido mensaje de entrega completada')
def mensaje_entrega_completada(context):
    assert bool(context.app.entregar_pedido_page.valido_entrega_completada())