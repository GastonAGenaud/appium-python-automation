# language: es

Característica: Estados Vacíos

    Escenario: Validación de pantalla "Visitados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Cuando selecciono "Visitados"
        Entonces valido el texto "Aun no visitas a ningun cliente"
        Y valido la pantalla de "Visitados"

    Escenario: Validación de pantalla "Anulados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Cuando selecciono "Anulados"
        Entonces valido el texto "No has anulado pedidos"
        Y valido la pantalla de "Anulados"

