from behave import given, when, then


@when('ingreso el correo electrónico "{correoElectronico}"')
def ingresar_correo(context, correoElectronico):
    context.app.login_page.ingresar_correo(correoElectronico)


@when('ingreso la contraseña "{contraseña}"')
def ingresar_contraseña(context, contraseña):
    context.app.login_page.ingresar_contraseña(contraseña)


@when('hago clic en el botón "Ingresar"')
def hacer_clic_ingresar(context):
    context.app.login_page.hacer_clic_ingresar()


@when('selecciono "{opcion}"')
def seleccionar_opcion(context, opcion):
    context.app.empty_states_page.seleccionar_estado(opcion)


@then('valido el texto "{texto}"')
def validar_texto(context, texto):
    assert context.app.empty_states_page.validar_texto_presente(texto)


@then('valido la pantalla de "{pantalla}"')
def validar_pantalla(context, pantalla):
    assert context.app.empty_states_page.validar_pantalla(pantalla)
