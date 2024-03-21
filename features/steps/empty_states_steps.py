from behave import given, when, then


@when('ingreso el correo electrónico "{correoElectronico}"')
def ingreso_el_correo_electronico(context, correoElectronico):
    context.empty_states_page.ingreso_el_correo_electronico(correoElectronico)


@when('selecciono "{opcion}"')
def seleccionar_opcion(context, opcion):
    context.empty_states_page.seleccionar_opcion(opcion)


@then('valido el texto "{texto}"')
def valido_el_texto(context, texto):
    assert context.empty_states_page.valido_el_texto(texto)


@then('valido la pantalla de "{pantalla}"')
def valido_la_pantalla(context, pantalla):
    assert context.empty_states_page.valido_la_pantalla(pantalla)
