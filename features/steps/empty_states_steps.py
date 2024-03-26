from behave import given, when, then


@when('selecciono "{opcion}"')
def seleccionar_opcion_visitados(context, opcion):
    context.app.empty_states_page.seleccionar_opcion_visitados()


@when('valido el texto "{texto}"')
def valido_el_texto_visitados(context, texto):
    assert context.app.empty_states_page.valido_el_texto_visitados(texto)


@then('valido la pantalla de "{pantalla}"')
def valido_la_pantalla(context, pantalla):
    assert context.empty_states_page.valido_la_pantalla(pantalla)
