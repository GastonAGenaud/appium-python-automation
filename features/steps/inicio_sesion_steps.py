from behave import given, when, then


@given('ingreso el correo electronico "{correo}"')
def ingresar_correo_electronico(context, correo):
    context.page_object.ingresar_correo_electronico(correo)


@given('ingreso la contraseña "{contraseña}"')
def ingresar_contraseña(context, contraseña):
    context.page_object.ingresar_contraseña(contraseña)


@when('hago clic en el botón "Ingresar"')
def hacer_clic_ingresar(context):
    context.page_object.hacer_clic_ingresar()


@then('se inicia sesion exitosamente')
def validar_inicio_sesion_exitoso(context):
    context.page_object.validar_mensaje_exito("Inicio de sesión exitoso")


@then('se valida el mensaje de error "{mensaje}"')
def validar_mensaje_error(context, mensaje):
    context.page_object.validar_mensaje_error_usuario_vacio(mensaje)


@then('se visualiza el mensaje de error "{mensaje}"')
def validar_mensaje_error_caracteres_especiales(context, mensaje):
    context.page_object.validar_mensaje_error_caracteres_especiales(mensaje)


@then('se visualiza el mensaje de error "{mensaje}"')
def validar_mensaje_error_contraseña_incorrecta(context, mensaje):
    context.page_object.validar_mensaje_error_contraseña_incorrecta(mensaje)


@then('se valida que el boton de "Login" este deshabilitado')
def validar_boton_login_deshabilitado(context):
    context.page_object.validar_boton_login_deshabilitado()


@then('se visualiza la pantalla de transporte "{mensaje_saludo}"')
def validar_pantalla_transporte(context, mensaje_saludo):
    context.page_object.validar_pantalla_transporte(mensaje_saludo)


@then('valido que la palabra "{palabra}" sea visible para la ruta "{ruta}"')
def validar_pantalla_transporte_en_curso(context, palabra, ruta):
    context.page_object.validar_pantalla_transporte_en_curso(palabra, ruta)


@then('valido que la palabra "{palabra}" sea visible')
def validar_pantalla_transporte_finalizado(context, palabra):
    context.page_object.validar_pantalla_transporte_finalizado(palabra)


@then('valido que la Vuelta sea "{texto_vuelta}"')
def validar_ruta_transporte(context, texto_vuelta):
    context.page_object.validar_ruta_transporte(texto_vuelta)


@then('valido que las Pallets sean "{texto_pallets}"')
def validar_pallets_transporte(context, texto_pallets):
    context.page_object.validar_pallets_transporte(texto_pallets)


@then('valido que los clientes sean "{texto_clientes}"')
def validar_clientes_transporte(context, texto_clientes):
    context.page_object.validar_clientes_transporte(texto_clientes)


@then('valido la pantalla de rutas no cargadas para hoy')
def validar_pantalla_rutas_no_cargadas(context):
    context.page_object.validar_pantalla_rutas_no_cargadas("No encontramos rutas cargadas para hoy")


@when('selecciono el botón "Actualizar"')
def hacer_clic_actualizar(context):
    context.page_object.hacer_clic_actualizar()


@then('valido que la aplicacion no tiene conexión')
def validar_no_conexion(context):
    context.page_object.validar_mensaje_no_conexion("No tienes conexión a internet")
