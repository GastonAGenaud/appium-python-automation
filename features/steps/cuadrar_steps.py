from behave import given, when, then


@given('ingreso el correo electrónico "{correo}"')
def ingreso_correo(context, correo):
    context.cuadrar_page.ingreso_correo(correo)


@given('ingreso la contraseña "{contraseña}"')
def ingreso_contraseña(context, contraseña):
    context.cuadrar_page.ingreso_contraseña(contraseña)


@when('hago clic en el botón "Ingresar"')
def clic_ingresar(context):
    context.cuadrar_page.clic_ingresar()


@when('elijo la ruta "{ruta}"')
def elegir_ruta(context, ruta):
    context.cuadrar_page.elegir_ruta(ruta)


@when('selecciono el botón "Comenzar ruta"')
def seleccionar_comenzar_ruta(context):
    context.cuadrar_page.seleccionar_comenzar_ruta()


@then('visualizo la pantalla "Ruta finalizada"')
def visualizar_pantalla_ruta_finalizada(context):
    assert context.cuadrar_page.visualizar_pantalla_ruta_finalizada()


@then('valido que el producto "{producto}" esté presente')
def producto_presente(context, producto):
    assert context.cuadrar_page.producto_presente(producto)


@then('valido el total como "{total}"')
def efectivo_valido(context, total):
    assert context.cuadrar_page.efectivo_valido(total)


@then('valido el total de transferencia como "{transferencia}"')
def validar_total_transferencia(context, transferencia):
    assert context.cuadrar_page.validar_total_transferencia(transferencia)


@then('valido el total de efectivo como "{efectivo}"')
def cheque_valido(context, efectivo):
    assert context.cuadrar_page.cheque_valido(efectivo)


@then('valido el total de cheque como "{cheque}"')
def validar_total_cheque(context, cheque):
    assert context.cuadrar_page.validar_total_cheque(cheque)


@then('valido el total de crédito como "{credito}"')
def credito_valido(context, credito):
    assert context.cuadrar_page.credito_valido(credito)


@then('valido el total rebajado como "{rebajado}"')
def rebajado_valido(context, rebajado):
    assert context.cuadrar_page.rebajado_valido(rebajado)


@then('valido la presencia del botón "Cerrar transporte"')
def boton_cerrar_transporte_presente(context):
    assert context.cuadrar_page.boton_cerrar_transporte_presente()


@then('valido que se muestre el mensaje "{mensaje}"')
def mensaje_transporte_listo(context, mensaje):
    assert context.cuadrar_page.mensaje_transporte_listo(mensaje)
