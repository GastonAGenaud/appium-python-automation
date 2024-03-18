Feature: Iniciar sesión

    Background:
        Given Voy a la pantalla de inicio de sesion

    Scenario Outline: Validacion de Iniciar sesion exitosamente
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        Then se inicia sesion exitosamente

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario: Validacion de error de campo de usuario
        When dejo el campo de Usuario vacio
        And hago click en el boton "Ingresar"
        Then se valida el mensaje de error "Tienes que ingresa un correo electronico"

    Scenario: Validacion de error de caracteres especiales
        When ingreso el correo electronico "Test$#@#!"
        And hago click en el boton "Ingresar"
        Then se visualiza el mensaje de error "No se admiten caracteres especiales"

    Scenario: Validacion de mensaje de error por contraseña incorrecta
        And hago click en el boton "Ingresar"
        Then se visualiza el mensaje de error "Correo o contraseña incorrectos"

            | correoElectronico |
            | test@test.com     |
            | Jonathan          |

    Scenario: Validacion de boton "Login" deshabilitado
        Given estoy en la pantalla de inicio de sesion
        When el boton de "Login" esta deshabilitado
        Then se valida que el boton de "Login" este deshabilitado

    Scenario Outline: Validacion de pantalla de transporte
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And visualizo la pantalla de transporte "<mensajeSaludo>"
        Then se visualizan los textos "<texto>" en la ruta "1222654"

        Examples:
            | mensajeSaludo  | texto    | contraseña | correoElectronico |
            | Hola Test!     | Test     | test123    | test@test.com     |
            | Hola Jonathan! | Jonathan | test123    | Jonathan          |
            | Hola Pedro!    | Pedro    | test123    | Pedro             |
            | Hola Maria!    | Maria    | test123    | Maria             |

    Scenario Outline: Validacion de pantalla de transporte en curso
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And visualizo la pantalla de transporte "Hola Jonathan!"
        When valido que la ruta "1222654" este en curso
        Then valido que la palabra "en curso" sea visible para la ruta "1222654"

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion de pantalla de transporte finalizado
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And visualizo la pantalla de transporte "Hola Jonathan!"
        Then valido que la palabra "finalizado" sea visible

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion de la ruta de transporte "<idRuta>"
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And valido que la Vuelta sea "<textoVuelta>"
        And valido que las Pallets sean "<textoPallets>"
        And valido que los clientes sean "<textoClientes>"

        Examples:
            | idRuta  | textoVuelta | textoPallets | textoClientes | correoElectronico |
            | 1222654 | 1 de 3      | 14           | 14            | Test              |
            | 4984379 | 1 de 1      | 12           | 2             | Test              |

    Scenario Outline: Validacion de pantalla de rutas no cargadas para hoy
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        When visualizo el texto "No encontramos rutas cargadas para hoy"
        And visiualizo el texto "Comunicate con mesa de ayuda"
        And selecciono el botón "Actualizar"
        Then valido la pantalla de rutas no cargadas para hoy

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario: Validacion de pantalla de no hay conexión
        And se visualiza el mensaje "No tienes conexion"
        And se visualiza el mensaje "Por favor revisa tu señal y tu conexion al wifi"
        And presiono el botón "Recargar"
        Then valido que la aplicacion no tiene conexión
