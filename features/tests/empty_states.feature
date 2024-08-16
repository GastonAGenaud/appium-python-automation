# language: es
@estados_vacios
Característica: Estados Vacíos

    @regresion
    Escenario: Validación de pantalla "Entregados"
        Dado Reseteo la app
        Y Ingreso con el conductor a la aplicacion
        Cuando selecciono la vuelta "Vuelta 1"
        Y hago click en el boton "Iniciar vuelta 1"
        Y selecciono "Entregados"
        Entonces valido la pantalla de "Entregados"

    @regresion
    Escenario: Validación de pantalla "Retornados"
        Dado Ingreso con el conductor a la aplicacion
        Cuando selecciono "Retornados"
        Entonces valido el texto "No has anulado pedidos"
        Y valido la pantalla de "Retornados"
