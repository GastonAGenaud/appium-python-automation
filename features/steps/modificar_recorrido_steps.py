from behave import given, when, then


@then('valido que se visualice el boton "{boton}"')
def valido_sea_visible_boton(context, boton):
    assert bool(context.app.modificar_recorrido_page.valido_comenzar_ruta_btn())


@then('valido que sea visible la "{caracteristica}" con el "{valor}" del pedido')
def valido_las_caracteristicas_valor(context, caracteristica, valor):
    assert bool(context.app.ux_page.valid_value(caracteristica, valor))


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


@then('valido que el texto {opcion} de la pantalla de modificacion manual')
def valido_texto_pantalla_modificacion_manual(context, opcion):
    if opcion == "Modifica tu ruta":
        assert bool(context.app.modificar_recorrido_page.valido_texto_modifica_tu_ruta())
    elif opcion == "Presiona prolongadamente":
        assert bool(context.app.modificar_recorrido_page.valido_texto_preiona_prolongadamente())
    elif opcion == "Entendido":
        assert bool(context.app.modificar_recorrido_page.valido_texto_entendido())
    elif opcion == "No volver a mostrar":
        assert bool(context.app.modificar_recorrido_page.valido_texto_no_volver_a_mostrar())
    else:
        raise ValueError(f"No se encontro el texto '{opcion}'")


@when('desplazo un cliente hacia una nueva posicion')
def desplazo_hacia_nueva_posicion(context):
    context.app.modificar_recorrido_page.drag_text_box_down()


@then('valido el mensaje que el cliente modifico su ubicacion hacia arriba en la lista')
def valido_mensaje_cliente_modificado(context):
    assert bool(context.app.modificar_recorrido_page.valido_mensaje_cliente_modificado_arriba())


@then('valido el mensaje que el cliente modifico su ubicacion hacia mas abajo en la lista')
def valido_mensaje_cliente_modificado_en_la_lista(context):
    assert bool(context.app.modificar_recorrido_page.valido_mensaje_cliente_modificado_abajo())
