from behave import given, when, then


@given("que el usuario ingresa un nombre")
def usuario_ingresa_un_nombre(context):
    context.app.login_page.user_input_name()


@given("el usuario ingresa una contrasena")
def usuario_ingresa_una_contrasena(context):
    context.app.login_page.user_input_password()


@when("el usuario permite el acceso a la ubicación de este dispositivo")
def usuario_permite_acceso_dispositivo(context):
    context.app.main_page.select_while_using_the_app()


@then("estoy en la página principal")
def usuario_en_pagina_principal(context):
    assert bool(context.app.main_page.valid_comenzar_ruta_button())


@then("valido que sea visible el botón Comenzar ruta")
def valido_sea_visible_comenzar_ruta(context):
    assert bool(context.app.main_page.valid_comenzar_ruta_button())


@then("valido que sea visible el botón Modificar manualmente")
def valido_sea_visible_modificar_manualmente(context):
    assert bool(context.app.main_page.valid_modificar_manualmente_btn())


@when("el usuario selecciona la sección Lista")
def usuario_selecciona_lista(context):
    context.app.main_page.select_lista_tab()


@then('valido que sea visible la "{caracteristica}" con el "{valor}" del pedido')
def valido_las_caracteristicas_valor(context, caracteristica, valor):
    assert bool(context.app.main_page.valid_value(caracteristica, valor))
