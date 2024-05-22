from behave import given, when, then


@then('valido el tamaño de zona de accion del boton "{boton}"')
def valido_tamano_zona_accion(context, boton):
    assert bool(context.app.UX_page.valido_tamano_ingresar_btn(boton))

    #if boton == "Ingresar":
    #    assert bool(context.app.inicio_sesion_page.valido_tamano_ingresar_btn())
    #elif boton == "Iniciar sesion":
    #    assert bool(context.app.inicio_sesion_page.valido_tamano_ingresar_btn())
    #elif boton == "Comenzar ruta":
    #    assert bool(context.app.inicio_sesion_page.valido_tamano_comenzar_ruta_btn())
    #else:
    #    raise ValueError(f"No se encontro el mensaje de error en el campo de '{boton}'")
