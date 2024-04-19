from behave import given, when, then


@then('valido que se visualice el boton "{boton}"')
def valido_sea_visible_boton(context, boton):
    assert bool(context.app.modificar_recorrido_page.valido_comenzar_ruta_btn())


@then('valido que sea visible la "{caracteristica}" con el "{valor}" del pedido')
def valido_las_caracteristicas_valor(context, caracteristica, valor):
    assert bool(context.app.modificar_recorrido_page.valid_value(caracteristica, valor))


@then('se valida que la ruta "{ruta}" este seleccionada')
def valida_ruta_seleccionada(context, ruta):
    assert bool(context.app.modificar_recorrido_page.valido_nro_factura())
