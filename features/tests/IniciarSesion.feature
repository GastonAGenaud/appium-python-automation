# language: es

Característica: Iniciar sesión

    Esquema del escenario: Validacion de Iniciar sesion exitosamente
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Entonces se inicia sesion exitosamente

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Escenario: Validacion de error de campo de usuario
        Dado dejo el campo de Usuario vacio
        Cuando hago click en el boton "Ingresar"
        Entonces se valida el mensaje de error "Tienes que ingresa un correo electronico"

    Escenario: Validacion de error de caracteres especiales
        Dado ingreso el correo electronico "Test$#@#!"
        Cuando hago click en el boton "Ingresar"
        Entonces se visualiza el mensaje de error "No se admiten caracteres especiales"

    Escenario: Validacion de mensaje de error por contraseña incorrecta
        Cuando hago click en el boton "Ingresar"
        Entonces se visualiza el mensaje de error "Correo o contraseña incorrectos"

            | correoElectronico |
            | test@test.com     |
            | Jonathan          |

    Escenario: Validacion de boton "Login" deshabilitado
        Dado estoy en la pantalla de inicio de sesion
        Cuando el boton de "Login" esta deshabilitado
        Entonces se valida que el boton de "Login" este deshabilitado

    Esquema del escenario: Validacion de pantalla de transporte
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y visualizo la pantalla de transporte "<mensajeSaludo>"
        Entonces se visualizan los textos "<texto>" en la ruta "1222654"

        Ejemplos:
            | mensajeSaludo  | texto    | contraseña | correoElectronico |
            | Hola Test!     | Test     | test123    | test@test.com     |
            | Hola Jonathan! | Jonathan | test123    | Jonathan          |
            | Hola Pedro!    | Pedro    | test123    | Pedro             |
            | Hola Maria!    | Maria    | test123    | Maria             |

    Esquema del escenario: Validacion de pantalla de transporte en curso
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y visualizo la pantalla de transporte "Hola Jonathan!"
        Y valido que la ruta "1222654" este en curso
        Entonces valido que la palabra "en curso" sea visible para la ruta "1222654"

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion de pantalla de transporte finalizado
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y visualizo la pantalla de transporte "Hola Jonathan!"
        Entonces valido que la palabra "finalizado" sea visible

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion de la ruta de transporte "<idRuta>"
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Entonces valido que la Vuelta sea "<textoVuelta>"
        Y valido que las Pallets sean "<textoPallets>"
        Y valido que los clientes sean "<textoClientes>"

        Ejemplos:
            | idRuta  | textoVuelta | textoPallets | textoClientes | correoElectronico |
            | 1222654 | 1 de 3      | 14           | 14            | Test              |
            | 4984379 | 1 de 1      | 12           | 2             | Test              |

    Esquema del escenario: Validacion de pantalla de rutas no cargadas para hoy
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Y visualizo el texto "No encontramos rutas cargadas para hoy"
        Y visiualizo el texto "Comunicate con mesa de ayuda"
        Cuando selecciono el botón "Actualizar"
        Entonces valido la pantalla de rutas no cargadas para hoy

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Escenario: Validacion de pantalla de no hay conexión
        Dado se visualiza el mensaje "No tienes conexion"
        Y se visualiza el mensaje "Por favor revisa tu señal y tu conexion al wifi"
        Cuando presiono el botón "Recargar"
        Entonces valido que la aplicacion no tiene conexión
