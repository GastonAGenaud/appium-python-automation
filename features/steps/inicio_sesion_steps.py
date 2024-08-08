import json
import os

from behave import given, when, then


@given('el usuario ingresa el correo electronico "{correo}"')
def usuario_ingresa_correo_electronico(context, correo):
    context.app.inicio_sesion_page.usuario_ingresa_correo_manual(correo)


@given("el usuario ingresa una contraseña")
def usuario_ingresa_una_contrasena(context):
    with open(os.path.join(context.basedir, 'config.json')) as config_file:
        config = json.load(config_file)
    context.app.inicio_sesion_page.usuario_ingresa_contrasena_manual(config['target']['password'])


@given('Ingreso con el conductor a la aplicacion')
def usuario_ingresa_aplicacion(context):
    if not context.logged_in:
        # Leer la configuración del archivo config.json
        with open(os.path.join(context.basedir, 'config.json')) as config_file:
            config = json.load(config_file)
        context.app.inicio_sesion_page.usuario_ingresa_correo(config['target']['usuario'], context.logged_in)
        context.app.inicio_sesion_page.usuario_ingresa_contrasena(config['target']['password'], context.logged_in)
        context.app.inicio_sesion_page.click_iniciar_sesion_btn(context.logged_in)
        context.logged_in = True


@when('hago click en el boton "{boton}"')
def click_en_el_boton(context, boton):
    if boton == "Iniciar sesion":
        context.app.inicio_sesion_page.click_iniciar_sesion_boton()
    elif boton == "Menu Lateral":
        context.app.inicio_sesion_page.click_menu_lateral_btn()
    elif boton == "Cerrar sesion":
        context.app.inicio_sesion_page.click_cerrar_sesion_btn()
    elif boton == "Cerrar aplicación":
        context.app.inicio_sesion_page.click_cerrar_aplicacion_btn()
    elif boton == "Sí, eliminar mi cuenta":
        context.app.inicio_sesion_page.click_si_eliminar_mi_cuenta_btn()
    elif boton == "Eliminar mi cuenta":
        context.app.inicio_sesion_page.click_eliminar_cuenta_btn()
    elif boton == "Terminos y condiciones":
        context.app.inicio_sesion_page.click_terminos_condiciones_btn()
    elif boton == "Aceptar términos y condiciones":
        context.app.inicio_sesion_page.click_aceptar_terminos_y_condiciones_btn()
    elif boton == "Retornar factura":
        context.app.revisar_pedido_page.click_retornar_factura_btn()
    elif boton == "Retornar todo":
        context.app.revisar_pedido_page.click_retornar_todo_btn()
    elif boton == "Entregar":
        context.app.revisar_pedido_page.click_entregar_btn()
    elif boton == "Aceptar":
        context.app.revisar_pedido_page.click_aceptar_boton()
    elif boton == "Confirmar":
        context.app.entregar_pedido_page.click_confirmar_boton()
    elif boton == "Confirmar modal":
        context.app.entregar_pedido_page.click_confirmar_2_btn()
    elif boton == "Confirmar widget":
        context.app.entregar_pedido_page.click_confirmarwidget_btn()
    elif boton == "Modificar":
        context.app.entregar_pedido_page.click_modificar_btn()
    elif boton == "Iniciar vuelta":
        context.app.modificar_recorrido_page.click_iniciar_vuelta_btn()
    elif boton == "Entendido":
        context.app.modificar_recorrido_page.click_entendido_boton()
    elif boton == "Desplegar":
        context.app.modificar_recorrido_page.click_desplegar_boton()
    elif boton == "Mover hacia arriba":
        context.app.modificar_recorrido_page.click_mover_hacia_arriba_boton()
    elif boton == "Mover a lo más abajo":
        context.app.modificar_recorrido_page.click_mover_a_lo_mas_abajo_boton()
    elif boton == "Cerrar vuelta 1":
        context.app.cuadrar_page.click_cerrar_vuelta_btn()
    elif boton == "Cerrar pedido":
        context.app.modificar_recorrido_page.click_cerrar_pedido_boton()
    elif boton == "Volver a mi ruta":
        context.app.entregar_pedido_page.click_volver_a_mi_ruta()
    elif boton == "Confirmar cierre de vueltas":
        context.app.cuadrar_page.click_confirmar_cierre_vueltas_btn()
    else:
        raise ValueError(f"No se encontro el boton de '{boton}'")


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
    assert bool(context.app.inicio_sesion_page.valid_mensaje_saludo())


@given('estoy en la pantalla de inicio de sesion')
def estoy_pantalla_de_inicio(context):
    assert bool(context.app.inicio_sesion_page.valido_pantalla_de_inicio())


@then('se valida que el boton de "{boton}" este deshabilitado')
def boton_login_deshabilitado(context, boton):
    assert not bool(context.app.inicio_sesion_page.valido_btn_ingresar_desactivado())


@when('hago click en el icono "{icono}"')
def hago_click_en_icono(context, icono):
    if icono == "back":
        context.app.inicio_sesion_page.click_icono_back()
    elif icono == "scroll down":
        context.app.inicio_sesion_page.click_scroll_down_icono()
    else:
        raise ValueError(f"No se encontro el icono de '{icono}'")


@then('Valido que la vuelta 1 fue iniciada')
def valido_vuelta_iniciada(context):
    assert bool(context.app.inicio_sesion_page.valido_vuelta_iniciada_txt())


@then('Valido la opcion Vuelta 1')
def valido_opcion_vuelta_1(context):
    assert context.app.inicio_sesion_page.opcion_vuelta_1_visible(), \
        "La opción 'Vuelta 1' no está visible en la pantalla"


@when('hago click en el boton "{boton}" en el modal')
def hago_click_en_boton_cerrar_sesion_modal(context, boton):
    context.app.inicio_sesion_page.click_cerrar_sesion_modal_btn()


@then('valido que se cerro la sesion')
def valido_sesion_cerrada(context):
    assert bool(context.app.inicio_sesion_page.valido_pantalla_de_inicio())


@then('valido que se aceptaron los terminos y condiciones')
def valido_aceptaron_los_terminos(context):
    assert bool(context.app.inicio_sesion_page.valido_mensaje_de_exito())


@then('valido que la cuenta se elimino exitosamente')
def valido_cuenta_elimino_exitosamente(context):
    assert bool(context.app.inicio_sesion_page.valido_cuenta_eliminada_txt())
