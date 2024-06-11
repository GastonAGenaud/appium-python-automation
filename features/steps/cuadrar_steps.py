from behave import then, when


@then('se valida el texto "{texto}"')
def validar_texto(context, texto):
    if texto == "25 clientes":
        assert bool(context.app.cuadrar_page.validar_texto_25_clientes())
    else:
        raise ValueError(f"Texto de validación no reconocido: {texto}")


@then('se valida el texto de la fecha')
def valido_modal_comenzar(context):
    assert bool(context.app.cuadrar_page.validar_texto_ruta_fecha())


@then('valido el modal de ruta comenzada')
def valido_modal_comenzar(context):
    assert context.app.cuadrar_page.validar_mensaje_comenzar()


@then('valido el Total esperado "{texto}"')
def valido_total_esperado(context, texto):
    assert bool(context.app.cuadrar_page.validar_precio_total_esperado())


@then('valido el Total recaudado "{texto}"')
def valido_total_recaudado(context, texto):
    assert bool(context.app.cuadrar_page.validar_precio_total_recaudado())


@then('valido el Total rebajado "{texto}"')
def valido_total_rebajado(context, texto):
    assert bool(context.app.cuadrar_page.validar_precio_total_rebajado())


@then('valido que por Transferencia el monto abonado es "{texto}"')
def valido_monto_por_transferencia(context, texto):
    assert bool(context.app.cuadrar_page.valido_monto_transferencia())


@then('valido que por Efectivo el monto abonado es "{texto}"')
def valido_monto_por_efectivo(context, texto):
    assert bool(context.app.cuadrar_page.valido_monto_efectivo())


@then('valido que por Cheque el monto abonado es "{texto}"')
def valido_monto_por_cheque(context, texto):
    assert bool(context.app.cuadrar_page.valido_monto_cheque())


@then('valido que por Credito el monto abonado es "{texto}"')
def valido_monto_por_credito(context, texto):
    assert bool(context.app.cuadrar_page.valido_monto_credito())


@then('valido que se muestre el mensaje "{texto}"')
def valido_mensaje_transporte_listo(context, texto):
    assert bool(context.app.cuadrar_page.valido_mensaje_de_transporte_listo())


@then('valido que las facturas fueron entregadas')
def valido_facturas_entregadas(context):
    assert bool(context.app.cuadrar_page.valido_factura_entregada_a())
    assert bool(context.app.cuadrar_page.valido_factura_entregada_b())


