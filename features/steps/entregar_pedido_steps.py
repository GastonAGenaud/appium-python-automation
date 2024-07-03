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


@when('selecciono el metodo que te van a pagar "{metodo}"')
def selecciono_metodo(context, metodo):
    if metodo == "efectivo":
        context.app.entregar_pedido_page.click_efectivo_checkbox()
    else:
        raise ValueError(f"No se encontro el metodo a pagar '{metodo}'")
