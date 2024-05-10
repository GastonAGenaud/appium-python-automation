# language: es

Característica: iniciar sesión

    Escenario: Validacion de Iniciar sesion exitosamente
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y hago click en el boton "Entendido"
        Entonces se inicia sesion exitosamente

    @smoke
    Escenario: Validacion de error por falta de correo
        Dado el usuario ingresa una contraseña
        Y valido el tamano de zona de accion del boton "Iniciar sesion"
        Cuando hago click en el boton "Iniciar sesion"
        Entonces se valida el mensaje de error en el campo de "correo electronico"

    @smoke
    Escenario: Validacion de mensaje de error por falta de contraseña
        Dado el usuario ingresa el correo electronico "user_tests"
        Cuando hago click en el boton "Iniciar sesion"
        Entonces se valida el mensaje de error en el campo de "contrasena"

    Escenario: Validacion de error de caracteres especiales
        Dado el usuario ingresa el correo electronico "Test$#@#!"
        Cuando hago click en el boton "Iniciar sesion"
        Entonces se valida el mensaje de error en el campo de "No se admiten caracteres especiales"

    Escenario: Validacion de boton "Login" deshabilitado
        Dado estoy en la pantalla de inicio de sesion
        Entonces se valida que el boton de "Login" este deshabilitado