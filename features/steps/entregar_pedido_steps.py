from behave import given, when, then


@when('selecciono para rebajar el pedido')
def rebajar_el_pedido(context):
    context.app.entregar_pedido_page.rebajo_el_pedido()


@then('valido mensaje de entrega completada')
def mensaje_entrega_completada(context):
    assert bool(context.app.entregar_pedido_page.valido_entrega_completada())


@when('cierro el cuadro de texto')
def cierro_cuadro_de_texto(context):
    context.app.entregar_pedido_page.click_cerrar_boton()


@when('selecciono pestaña de "{texto}"')
def selecciono_entregados(context, texto):
    context.app.entregar_pedido_page.click_seccion_entregados()
