from behave import then, when


@then('se valida el texto "{texto}"')
def validar_texto(context, texto):
    if texto == "RUTA 20 MAYO":
        assert bool(context.app.cuadrar_page.validar_texto_ruta_mayo())
    elif texto == "25 clientes":
        assert bool(context.app.cuadrar_page.validar_texto_25_clientes())
    else:
        raise ValueError(f"Texto de validación no reconocido: {texto}")


@then('valido el modal de ruta comenzada')
def valido_modal_comenzar(context):
    assert context.app.cuadrar_page.validar_mensaje_comenzar()

