from behave import given, when, then


@when('selecciono "{seccion}"')
def selecciono_seccion(context, seccion):
    if seccion == 'Anulados':
        context.app.empty_states_page.seccion_anulados()
    elif seccion == 'Retornados':
        context.app.empty_states_page.seccion_retornados()
    elif seccion == 'Entregados':
        context.app.empty_states_page.seccion_entregados()
    elif seccion == 'Visitados':
        context.app.empty_states_page.seccion_visitados()
    elif seccion == 'Rebajados':
        context.app.empty_states_page.seccion_rebajados()
    else:
        raise ValueError(f"No se encontro la seccion '{seccion}'")


@when('selecciono el sector "{seccion}"')
def selecciono_seccion(context, seccion):
    if seccion == 'Entregados':
        context.app.empty_states_page.sector_entregados()
    elif seccion == 'Retornados':
        context.app.empty_states_page.seccion_retornados()
    else:
        raise ValueError(f"No se encontro la seccion '{seccion}'")


@then('valido el texto "{texto}"')
def valido_texto(context, texto):
    if texto == 'No has anulado pedidos':
        assert bool(context.app.empty_states_page.valido_txt_seccion_anulados())
    elif texto == 'Aun no visitas a ningun cliente':
        assert bool(context.app.empty_states_page.no_has_visitado_clientes_txt())
    elif texto == 'Entregada':
        assert context.app.cuadrar_page.validar_texto_entregada()
    elif texto == 'No hay productos rebajados':
        assert context.app.cuadrar_page.validar_texto_no_hay_producto()
    elif texto == 'Entrega impecable':
        assert bool(context.app.cuadrar_page.valido_mensaje_entrega_impecable())
    elif texto == '¡Felicitaciones! Has entregado el pedido sin rebajas. Que siga la buena racha.':
        assert bool(context.app.cuadrar_page.validar_entrega_exitosa_texto())
    else:
        raise ValueError(f"No se encontró el texto '{texto}'")


@then('valido la pantalla de "{pantalla}"')
def valido_pantalla(context, pantalla):
    if pantalla == 'Anulados':
        assert bool(context.app.empty_states_page.valido_imagen_seccion_anulados())
    elif pantalla == 'Retornados':
        assert bool(context.app.empty_states_page.valido_imagen_seccion_anulados())
    elif pantalla == 'Visitados':
        assert bool(context.app.empty_states_page.imagen_seccion_visitados())
    elif pantalla == 'Entregados':
        assert bool(context.app.empty_states_page.valido_seccion_entregados())
    else:
        raise ValueError(f"No se pudo validar la siguiente pantalla '{pantalla}'")
