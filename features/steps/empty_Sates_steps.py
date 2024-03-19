from behave import given, when, then


@when('ingreso el correo electrónico "{correoElectronico}"')
def ingresar_correo(context, correoElectronico):
    return True


@when('ingreso la contraseña "{contraseña}"')
def ingresar_contraseña(context, contraseña):
    return True


@when('selecciono "{opcion}"')
def seleccionar_opcion(context, opcion):
    return True


@then('valido el texto "{texto}"')
def validar_texto(context, texto):
    return True


@then('valido la pantalla de "{pantalla}"')
def validar_pantalla(context, pantalla):
    return True
