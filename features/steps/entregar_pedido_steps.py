from behave import given, when, then


@when('selecciono para rebajar el pedido')
def rebajar_el_pedido(context):
    context.app.entregar_pedido_page.rebajo_el_pedido()


@then('valido el total de la factura como "{precio}"')
def valido_el_total_de_factura(context, precio):
    assert context.app.entregar_pedido_page.valido_precio_total_factura(
        precio), f"El total de la factura no es {precio}"


@then('valido el total rebajado como "{precio}"')
def valido_el_total_rebajado(context, precio):
    assert context.app.entregar_pedido_page.valido_precio_rebajado(precio), f"El total rebajado no es {precio}"


@then('valido mensaje de entrega completada')
def mensaje_entrega_completada(context):
    assert context.app.entregar_pedido_page.valido_entrega_completada(), "El mensaje de entrega completada no es visible"


@then('valido el botón "Confirmar"')
def valido_boton_volver_a_mi_ruta(context):
    assert context.app.cuadrar_page.valido_confirmar_btn(), 'El botón "Confirmar" no es visible'


@then('valido el icono de la pantalla "Entrega impecable"')
def valido_icono_entrega_impecable(context):
    assert context.app.entregar_pedido_page.valido_icono_entregar_pedido(), 'El icono de "Entrega impecable" no es visible'


@then('Valido el pedido entregado correctamente')
def valido_productos_en_entregados(context):
    assert context.app.empty_states_page.productos_en_entregados(), "El pedido no se entregó correctamente"


@then('valido la pantalla y textos de "Entregados"')
def validar_pantalla_y_textos_entregados(context):
    assert context.app.entregar_pedido_page.validar_pantalla_y_textos_entregados(), "La pantalla o los textos de 'Entregados' no son visibles."


@when('hago click en el boton "Confirmar" de la pantalla Felicitaciones')
def click_confirmar_entrega(context):
    context.app.entregar_pedido_page.click_confirmar_entrega()


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
