# language: es

Característica: Estados Vacíos

    @regresion
    Escenario: Validación de pantalla "Entregados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y selecciono "Entregados"
        Entonces valido la pantalla de "Entregados"

    @regresion
    Escenario: Validación de pantalla "Retornados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y selecciono "Retornados"
        Entonces valido el texto "No has anulado pedidos"
        Y valido la pantalla de "Retornados"

