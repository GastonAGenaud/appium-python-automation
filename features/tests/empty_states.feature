# language: es
@estados_vacios
Característica: Estados Vacíos

    @regresion
    Escenario: Validación de pantalla "Entregados"
        Dado Ingreso con el conductor a la aplicacion
        Cuando selecciono "Entregados"
        Entonces valido la pantalla de "Entregados"

    @regresion
    Escenario: Validación de pantalla "Retornados"
        Dado Ingreso con el conductor a la aplicacion
        Cuando selecciono "Retornados"
        Entonces valido el texto "No has anulado pedidos"
        Y valido la pantalla de "Retornados"
