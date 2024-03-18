from behave import given, when, then


@when('ingreso el correo electrónico "{correoElectronico}"')
def ingresar_correo(context, correoElectronico):
    return True


@when('ingreso la contraseña "{contraseña}"')
def ingresar_contraseña(context, contraseña):
    return True


@when('hago clic en el botón "Ingresar"')
def hacer_clic_ingresar(context):
    return True


@when('elijo la ruta "{nombreRuta}"')
def elegir_ruta(context, nombreRuta):
    return True


@when('selecciono el botón "Comenzar ruta"')
def seleccionar_comenzar_ruta(context):
    return True


@then('valido que se muestre la pantalla "Ruta finalizada"')
def validar_pantalla_ruta_finalizada(context):
    return True


@then('valido que el producto "{nombreProducto}" esté presente')
def validar_producto_presente(context, nombreProducto):
    return True


@then('valido el total como "{cantidad}" "{totalEsperado}"')
def validar_total(context, cantidad, totalEsperado):
    return True


@then('valido la presencia del botón "Cerrar transporte"')
def validar_presencia_boton_cerrar_transporte(context):
    return True


@then('valido que se muestre el mensaje "{mensajeEsperado}"')
def validar_mensaje_transporte_listo(context, mensajeEsperado):
    return True
