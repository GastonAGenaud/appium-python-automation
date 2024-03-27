# language: es

Característica: iniciar sesión

    Escenario: Validacion de Iniciar sesion exitosamente
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Cuando hago click en el boton "Ingresar"
        Y hago click en el boton "Entendido"
        Entonces se inicia sesion exitosamente

    @smoke
    Escenario: Validacion de error por falta de correo
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y valido el tamano de zona de accion del boton "Ingresar"
        Cuando hago click en el boton "Ingresar"
        Entonces se valida el mensaje de error en el campo de "correo electronico"

    @smoke
    Escenario: Validacion de mensaje de error por falta de contrasena
        Dado el usuario ingresa el correo electronico "user_tests"
        Cuando hago click en el boton "Ingresar"
        Entonces se valida el mensaje de error en el campo de "contrasena"

    Escenario: Validacion de error de caracteres especiales (*)
        Dado el usuario ingresa el correo electronico "Test$#@#!"
        Cuando hago click en el boton "Ingresar"
        Entonces se valida el mensaje de error en el campo de "No se admiten caracteres especiales"

    Escenario: Validacion de boton "Login" deshabilitado
        Dado estoy en la pantalla de inicio de sesion
        Entonces se valida que el boton de "Login" este deshabilitado

#    Escenario: Validacion de pantalla de transporte
#        Dado ingreso el correo electronico "<correoElectronico>"
#        Y ingreso la contraseña "<contraseña>"
#        Cuando hago click en el boton "Ingresar"
#        Y visualizo la pantalla de transporte "<mensajeSaludo>"
#        Entonces se visualizan los textos "<texto>" en la ruta "1222654"

#    Escenario: Validacion de pantalla de transporte en curso
#        Dado ingreso el correo electronico "<correoElectronico>"
#        Y ingreso la contraseña "<contraseña>"
#        Cuando hago click en el boton "Ingresar"
#        Y visualizo la pantalla de transporte "Hola Jonathan!"
#        Y valido que la ruta "1222654" este en curso
#        Entonces valido que la palabra "en curso" sea visible para la ruta "1222654"

#    Escenario: Validacion de pantalla de transporte finalizado
#        Dado ingreso el correo electronico "<correoElectronico>"
#        Y ingreso la contraseña "<contraseña>"
#        Cuando hago click en el boton "Ingresar"
#        Y visualizo la pantalla de transporte "Hola Jonathan!"
#        Entonces valido que la palabra "finalizado" sea visible


#    Escenario: Validacion de la ruta de transporte "<idRuta>"
#        Dado ingreso el correo electronico "<correoElectronico>"
#        Y ingreso la contraseña "<contraseña>"
#        Cuando hago click en el boton "Ingresar"
#        Entonces valido que la Vuelta sea "<textoVuelta>"
#        Y valido que las Pallets sean "<textoPallets>"
#        Y valido que los clientes sean "<textoClientes>"

#    Escenario: Validacion de pantalla de rutas no cargadas para hoy
#        Dado ingreso el correo electronico "<correoElectronico>"
#        Y ingreso la contraseña "<contraseña>"
#        Y visualizo el texto "No encontramos rutas cargadas para hoy"
#        Y visiualizo el texto "Comunicate con mesa de ayuda"
#        Cuando selecciono el botón "Actualizar"
#        Entonces valido la pantalla de rutas no cargadas para hoy

#    Escenario: Validacion de pantalla de no hay conexión
#        Dado se visualiza el mensaje "No tienes conexion"
#        Y se visualiza el mensaje "Por favor revisa tu señal y tu conexion al wifi"
#        Cuando presiono el botón "Recargar"
#        Entonces valido que la aplicacion no tiene conexión
