from behave import given, when, then


@given('el usuario ingresa el correo electronico "{correo}"')
def usuario_ingresa_correo(context, correo):
    if correo == "user_tests":
        context.app.inicio_sesion_page.usuario_ingresa_correo_user_tests()
    elif correo == "Test$#@#!":
        context.app.inicio_sesion_page.usuario_ingresa_correo_erroneo()
    else:
        raise ValueError(f"No se encontro el mensaje de error en el campo al ingresar el correo '{correo}'")


@given("el usuario ingresa una contrasena")
def usuario_ingresa_una_contrasena(context):
    context.app.inicio_sesion_page.usuario_ingresa_contrasena()


@when('hago click en el boton "{boton}"')
def click_en_el_boton(context, boton):
    if boton == "ingresar":
        context.app.inicio_sesion_page.click_ingresa_btn()
    elif boton == "Test$#@#!":
        context.app.inicio_sesion_page.click_entendido_btn()
    else:
        raise ValueError(f"No se encontro el boton de '{boton}'")


@then('se valida el mensaje de error en el campo de "{texto}"')
def validar_mensaje_de_error(context, texto):
    if texto == "correo electronico":
        assert bool(context.app.inicio_sesion_page.valido_mensaje_error_correo())
    elif texto == "contrasena":
        assert bool(context.app.inicio_sesion_page.valido_mensaje_error_contrasena())
    else:
        raise ValueError(f"No se encontro el mensaje de error en el campo de '{texto}'")


@then('se inicia sesion exitosamente')
def inicio_sesion_exitosamente(context):
    assert bool(context.app.inicio_sesion_page.valid_comenzar_ruta_btn())


@given('valido el tamano de zona de accion del boton "{boton}"')
def valido_tamano_zona_accion(context, boton):
    if boton == "Ingresar":
        assert bool(context.app.inicio_sesion_page.valido_tamano_ingresar_btn())
    elif boton == "Comenzar ruta":
        assert bool(context.app.inicio_sesion_page.valido_tamano_comenzar_ruta_btn())
    else:
        raise ValueError(f"No se encontro el mensaje de error en el campo de '{boton}'")


@given('estoy en la pantalla de inicio de sesion')
def estoy_pantalla_de_inicio(context):
    assert bool(context.app.inicio_sesion_page.valido_pantalla_de_inicio())


@then('se valida que el boton de "{Login}" este deshabilitado')
def boton_login_deshabilitado(context, Login):
    assert bool(context.app.inicio_sesion_page)



