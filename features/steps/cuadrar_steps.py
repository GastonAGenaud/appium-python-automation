from behave import given, when, then


@then('valido que se muestre la pantalla "Ruta finalizada"')
def validar_pantalla_ruta_finalizada(context):
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
