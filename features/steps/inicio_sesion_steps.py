from behave import given, when, then


@given('el usuario ingresa el correo electronico "{correo}"')
def usuario_ingresa_correo(context, correo):
    context.app.inicio_sesion_page.usuario_ingresa_correo(correo)


@given("el usuario ingresa una contraseña")
def usuario_ingresa_una_contrasena(context):
    context.app.inicio_sesion_page.usuario_ingresa_contrasena()


@when('hago click en el boton "{boton}"')
def click_en_el_boton(context, boton):
    if boton == "Ingresar":
        context.app.inicio_sesion_page.click_ingresa_btn()
    elif boton == "Iniciar sesion":
        context.app.inicio_sesion_page.click_iniciar_sesion_btn()
    elif boton == "Test$#@#!":
        context.app.inicio_sesion_page.click_entendido_btn()
    elif boton == "Anular pedido":
        context.app.revisar_pedido_page.click_anular_pedido_btn()
    elif boton == "Retornar pedido":
        context.app.revisar_pedido_page.click_retornar_pedido_btn()
    elif boton == "Entregar":
        context.app.revisar_pedido_page.click_entregar_btn()
    elif boton == "entregar":
        context.app.revisar_pedido_page.click_entregar_boton()
    elif boton == "Confirmar":
        context.app.entregar_pedido_page.click_confirmar_boton()
    elif boton == "Modificar":
        context.app.entregar_pedido_page.click_modificar_btn()
    elif boton == "Comenzar ruta":
        context.app.modificar_recorrido_page.click_comenzar_ruta_btn()
    elif boton == "Entendido":
        context.app.modificar_recorrido_page.click_entendido_boton()
    elif boton == "Desplegar":
        context.app.modificar_recorrido_page.click_desplegar_boton()
    elif boton == "Mover hacia arriba":
        context.app.modificar_recorrido_page.click_mover_hacia_arriba_boton()
    elif boton == "Mover a lo más abajo":
        context.app.modificar_recorrido_page.click_mover_a_lo_mas_abajo_boton()
    elif boton == "Retornados":
        context.app.anular_pedido_page.selecciono_boton_retornado()
    elif boton == "Cerrar transporte":
        context.app.cuadrar_page.click_cerrar_transporte_btn()
    elif boton == "Volver a mi ruta":
        context.app.entregar_pedido_page.click_volver_a_mi_ruta()
    else:
        raise ValueError(f"No se encontro el boton de '{boton}'")


@then("hago click en el boton Confirmar")
def click_en_boton_Confirmar(context):
    context.app.entregar_pedido_page.click_confirmar_boton()


@then('se valida el mensaje de error en el campo de "{texto}"')
def validar_mensaje_de_error(context, texto):
    if texto == "correo electronico":
        assert bool(context.app.inicio_sesion_page.valido_mensaje_error_correo())
    elif texto == "contrasena":
        assert bool(context.app.inicio_sesion_page.valido_mensaje_error_contrasena())
    else:
        raise ValueError(f"No se encontro el mensaje de error en el campo de '{texto}'")


@then('se inicia sesion exitosamente')
def inicio_sesion_exitosamente(context):
    assert bool(context.app.inicio_sesion_page.valid_comenzar_ruta_btn())


@given('estoy en la pantalla de inicio de sesion')
def estoy_pantalla_de_inicio(context):
    assert bool(context.app.inicio_sesion_page.valido_pantalla_de_inicio())


@then('se valida que el boton de "{boton}" este deshabilitado')
def boton_login_deshabilitado(context, boton):
    assert not bool(context.app.inicio_sesion_page.valido_btn_ingresar_desactivado())
