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


@then('valido el botón "Volver a mi ruta"')
def valido_boton_volver_a_mi_ruta(context):
    assert bool(context.app.cuadrar_page.valido_volver_mi_ruta())


@then('valido el icono de la pantalla "Entrega impecable"')
def valido_icono_entrega_impecable(context):
    assert bool(context.app.entregar_pedido_page.valido_icono_entregar_pedido())


@then('Valido el pedido entregado correctamente')
def valido_productos_en_entregados(context):
    assert context.app.empty_states_page.productos_en_entregados()


@when('cierro el cuadro de texto')
def cierro_cuadro_de_texto(context):
    context.app.entregar_pedido_page.click_cerrar_boton()