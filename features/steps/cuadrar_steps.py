# -*- coding: utf-8 -*-

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


@when('elijo la ruta "{nombreRuta}"')
def elegir_ruta(context, nombreRuta):
    context.app.route_page.seleccionar_ruta(nombreRuta)


@when('selecciono el botón "Comenzar ruta"')
def seleccionar_comenzar_ruta(context):
    context.app.route_page.hacer_clic_comenzar_ruta()


@then('valido que se muestre la pantalla "Ruta finalizada"')
def validar_pantalla_ruta_finalizada(context):
    assert context.app.finalized_route_page.is_open()


@then('valido que el producto "{nombreProducto}" esté presente')
def validar_producto_presente(context, nombreProducto):
    context.app.finalized_route_page.validar_producto_presente(nombreProducto)


@then('valido el total como "{cantidad}" "{totalEsperado}"')
def validar_total(context, cantidad, totalEsperado):
    context.app.finalized_route_page.validar_total(cantidad, totalEsperado)


@then('valido la presencia del botón "Cerrar transporte"')
def validar_presencia_boton_cerrar_transporte(context):
    context.app.finalized_route_page.validar_botón_cerrar_transporte_presente()


@then('valido que se muestre el mensaje "{mensajeEsperado}"')
def validar_mensaje_transporte_listo(context, mensajeEsperado):
    context.app.finalized_route_page.validar_mensaje_transporte_listo(mensajeEsperado)
