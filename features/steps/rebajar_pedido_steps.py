from behave import given, when, then


@then('verifico pantalla del producto rebajado')
def valido_texto_retornar(context):
    assert context.app.rebajar_pedido_page.retornado_sobre_stock


@then('valido la presencia de los motivos de anulacion')
def validar_presencia_motivos_anulados(context):
    motivos = [row['motivo'] for row in context.table]
    assert context.app.rebajar_pedido_page.motivo_anulacion_pantalla_lista(motivos), \
        "No todos los motivos de anulacion están presentes en la pantalla"
