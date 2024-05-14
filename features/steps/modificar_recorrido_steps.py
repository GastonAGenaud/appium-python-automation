from behave import given, when, then


@then('valido que se visualice el boton "{boton}"')
def valido_sea_visible_boton(context, boton):
    assert bool(context.app.modificar_recorrido_page.valido_comenzar_ruta_btn())


@then('valido que sea visible la "{caracteristica}" con el "{valor}" del pedido')
def valido_las_caracteristicas_valor(context, caracteristica, valor):
    assert bool(context.app.modificar_recorrido_page.valid_value(caracteristica, valor))


@then('se valida que la ruta "{ruta}" este seleccionada')
def valida_ruta_seleccionada(context, ruta):
    assert bool(context.app.modificar_recorrido_page.valido_el_deseo_spa_local())


@when('hago click en el desplegable')
def hago_click_desplegable(context):
    context.app.modificar_recorrido_page.click_desplegador_btn()


@then('valido que sea visible la opcion "{opcion}"')
def valido_las_opcion(context, opcion):
    if opcion == "Mas productos":
        assert bool(context.app.modificar_recorrido_page.valido_mas_productos_opcion())
    elif opcion == "Menos productos":
        assert bool(context.app.modificar_recorrido_page.valido_menos_productos_opcion())
    elif opcion == "Ruta sugerida":
        assert bool(context.app.modificar_recorrido_page.valido_menos_productos_opcion())
    else:
        raise ValueError(f"No se encontro la opcion '{opcion}'")


@then('se valida que el boton {boton} haya sido seleccionado correctamente')
def valido_boton(context, boton):
    assert bool(context.app.modificar_recorrido_page.valido_comenzar_ruta_msg())


@then('valido que el texto {texto} de la pantalla de modificacion manual')
def valido_texto_pantalla_modificacion_manual(context, texto):
    if texto == "Modifica tu ruta":
        assert bool(context.app.modificar_recorrido_page.valido_texto_modifica_tu_ruta())
    elif texto == "Presiona prolongadamente":
        assert bool(context.app.modificar_recorrido_page.valido_texto_preiona_prolongadamente())
    elif texto == "Entendido":
        assert bool(context.app.modificar_recorrido_page.valido_texto_entendido())
    elif texto == "No volver a mostrar":
        assert bool(context.app.modificar_recorrido_page.valido_texto_no_volver_a_mostrar())
    else:
        raise ValueError(f"No se encontro el texto '{texto}'")



