import re

from behave import given, when, then
from features.pages.inicio_sesion_page import LoginPage


@given('ingreso el correo electronico "{correo}"')
def ingresar_correo_electronico(context, correo):
    context.app.inicio_sesion_page.ingresar_correo_electronico(correo)


@given('ingreso la contrasena "{contrasena}"')
def ingresar_contrasena(context, contrasena):
    context.app.inicio_sesion_page.ingresar_contrasena(contrasena)


@then('se inicia sesion exitosamente')
def validar_inicio_sesion_exitoso(context):
    boton_comenzar_ruta = context.app.inicio_sesion_page.boton_comenzar_ruta()
    assert boton_comenzar_ruta


@then('se valida el mensaje de error "{mensaje}"')
def validar_mensaje_error(context, mensaje):
    context.app.inicio_sesion_page.validar_mensaje_error_usuario_vacio(mensaje)


@then('se visualiza el mensaje de error "{mensaje}"')
def validar_mensaje_error_contrasena_incorrecta(context, mensaje):
    context.app.inicio_sesion_page.validar_mensaje_error_contrasena_incorrecta(mensaje)


@then('se valida que el boton de "Login" este deshabilitado')
def validar_boton_login_deshabilitado(context):
    context.app.inicio_sesion_page.validar_boton_login_deshabilitado()


@then('se visualiza la pantalla de transporte "{mensaje_saludo}"')
def validar_pantalla_transporte(context, mensaje_saludo):
    context.app.inicio_sesion_page.validar_pantalla_transporte(mensaje_saludo)


@then('valido que la palabra "{palabra}" sea visible para la ruta "{ruta}"')
def validar_pantalla_transporte_en_curso(context, palabra, ruta):
    context.app.inicio_sesion_page.validar_pantalla_transporte_en_curso(palabra, ruta)


@then('valido que la palabra "{palabra}" sea visible')
def validar_pantalla_transporte_finalizado(context, palabra):
    context.app.inicio_sesion_page.validar_pantalla_transporte_finalizado(palabra)


@then('valido que la Vuelta sea "{texto_vuelta}"')
def validar_ruta_transporte(context, texto_vuelta):
    context.app.inicio_sesion_page.validar_ruta_transporte(texto_vuelta)


@then('valido que las Pallets sean "{texto_pallets}"')
def validar_pallets_transporte(context, texto_pallets):
    context.app.inicio_sesion_page.validar_pallets_transporte(texto_pallets)


@then('valido que los clientes sean "{texto_clientes}"')
def validar_clientes_transporte(context, texto_clientes):
    context.app.inicio_sesion_page.validar_clientes_transporte(texto_clientes)


@then('valido la pantalla de rutas no cargadas para hoy')
def validar_pantalla_rutas_no_cargadas(context):
    context.app.inicio_sesion_page.validar_pantalla_rutas_no_cargadas("No encontramos rutas cargadas para hoy")


@when('selecciono el botón "Actualizar"')
def hacer_clic_actualizar(context):
    context.app.inicio_sesion_page.hacer_clic_actualizar()


@then('valido que la aplicacion no tiene conexión')
def validar_no_conexion(context):
    context.app.inicio_sesion_page.validar_mensaje_no_conexion("No tienes conexión a internet")


@when('hago click en el boton "{boton}"')
def click_boton(context, boton):
    boton = boton.lower()
    if boton == "ingresar":
        context.app.inicio_sesion_page.hacer_clic_ingresar()
    elif boton == "entendido":
        context.app.inicio_sesion_page.click_boton_entendido()
    else:
        raise ValueError(f"No se puede hacer clic en el botón '{boton}'")


@given("dejo el campo de Usuario vacio")
def campo_vacio(context):
    context.app.inicio_sesion_page.limpiar_campo_usuario()


@then('se visualiza el mensaje de error de caracteres especiales "{mensaje}"')
def validar_mensaje_error_caracteres_especiales(context, mensaje):
    context.app.inicio_sesion_page.validar_mensaje_error_caracteres_especiales(mensaje)
