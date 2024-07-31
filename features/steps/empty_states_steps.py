import time

from behave import given, when, then


@when('selecciono "{seccion}"')
def selecciono_seccion(context, seccion):
    if seccion == 'Retornados':
        context.app.empty_states_page.seccion_retornados()
    elif seccion == 'Entregados':
        context.app.empty_states_page.seccion_entregados()
    elif seccion == 'Sobre stock':
        context.app.anular_pedido_page.seleccionar_nombre(seccion)
    else:
        raise ValueError(f"No se encontro la seccion '{seccion}'")


@then('valido el texto "{texto}"')
def valido_texto(context, texto):
    if texto == 'No has anulado pedidos':
        assert bool(context.app.empty_states_page.valido_txt_seccion_anulados())
    elif texto == 'Aun no visitas a ningun cliente':
        assert bool(context.app.empty_states_page.no_has_visitado_clientes_txt())
    elif texto == 'Entregada':
        assert context.app.cuadrar_page.validar_texto_entregada()
    elif texto == 'No hay productos rebajados':
        assert context.app.cuadrar_page.validar_texto_no_hay_producto()
    elif texto == '¿Con qué te van a pagar?':
        assert context.app.revisar_pedido_page.valido_titulo_metodo_de_pago()
    elif texto == 'Entrega impecable':
        assert bool(context.app.cuadrar_page.valido_mensaje_entrega_impecable())
    elif texto == '¡Felicitaciones! Has entregado el pedido sin rebajas. Que siga la buena racha.':
        assert bool(context.app.cuadrar_page.validar_entrega_exitosa_texto())
    elif texto == 'Buenas tardes':
        assert bool(context.app.inicio_sesion_page.valid_mensaje_saludo())
    elif texto == 'Estas son tus vueltas disponibles':
        assert bool(context.app.inicio_sesion_page.valid_titulo_vueltas_disponible())
    else:
        raise ValueError(f"No se encontró el texto '{texto}'")


@then('valido la pantalla de "{pantalla}"')
def valido_pantalla(context, pantalla):
    if pantalla == 'Retornados':
        assert bool(context.app.empty_states_page.valido_imagen_seccion_anulados())
    elif pantalla == 'Entregados':
        assert bool(context.app.empty_states_page.valido_seccion_entregados())
    else:
        raise ValueError(f"No se pudo validar la siguiente pantalla '{pantalla}'")


@given('Reseteo la app')
def reseteo_app(context):
    package_name = "com.rutadigital"

    # Terminar la app
    context.driver.terminate_app(package_name)
    # Esperar un momento para asegurarse de que la app esté completamente cerrada
    time.sleep(5)
    # Abrir la app nuevamente
    context.driver.activate_app(package_name)
    context.logged_in = False
