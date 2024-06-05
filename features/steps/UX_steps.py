from behave import given, when, then


@then('valido el tamaño de zona de accion del boton "{boton}"')
def valido_tamano_zona_accion(context, boton):
    assert bool(context.app.ux_page.valido_tamano_ingresar_btn(boton))


@then('valido la captura de pantalla del elemento "{xpath}"')
def valido_captura_pantalla(context, xpath):
    ruta_captura = context.app.ux_page.capturar_captura_elemento(xpath)
    assert ruta_captura is not None


@then('valido la pantalla con la imagen de referencia "{xpath}" "{ruta_referencia}"')
def valido_pantalla_con_referencia(context, xpath, ruta_referencia):
    ruta_captura = context.app.ux_page.capturar_captura_elemento(xpath)
    assert context.app.ux_page.comparar_imagenes(ruta_captura, ruta_referencia)
