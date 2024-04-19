# language: es

Característica: Modificar recorrido sugerido

    Escenario: Validacion de la pantalla Comenzar ruta
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Cuando hago click en el boton "Ingresar"
        Entonces valido que se visualice el boton "Comenzar ruta"

    Esquema del escenario: Validacion de la ruta
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Entonces valido que sea visible la "<caracteristica>" con el "<valor>" del pedido

        Ejemplos:
            | caracteristica | valor                 |
            | Local          | Pudahuel              |
            | Horario        | Cierra a las 14:00:00 |
            | Producto       | 20                    |
            | Efectivo       | $50.000               |

    Escenario: Validacion de seleccion de ruta
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Y elijo la ruta "Pudahuel"
        Entonces se valida que la ruta "Pudahuel" este seleccionada

    Escenario: Validacion del boton "Comenzar ruta"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        #Y elijo la ruta "1222654"
        Y hago click en el boton "Comenzar ruta"
        #Entonces se valida que el boton "Comenzar ruta" haya sido seleccionado correctamente

    Escenario: Validacion del desplegable "Mas productos"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        #Y elijo la ruta "1222654"
        #Entonces valido la informacion:
        #    | Texto         |
        #    | Ruta sugerida |
        #    | Mas lejos |
        #    | Mas cerca |

    Escenario: Validacion de pantalla de modificar manualmente
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Y selecciono el boton "Modificar manualmente"
        Entonces valido la informacion del texto de la pantalla de modificacion manual
            | Texto                    |
            | Modifica tu ruta         |
            | Presiona prolongadamente |
            | Entendido                |
            | No volver a mostrar      |

    Escenario: Validacion de la modificacion de la ruta
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Y selecciono el boton "Modificar manualmente"
        Y selecciono el boton "Entendido"
        Y desplazo un cliente hacia una nueva posicion
        Entonces valido el mensaje "Recorrido modificado"

    Escenario: Validacion de opcion "Pendientes"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Entonces valido la funcionalidad del boton "Pendientes"

    Escenario: Validacion de opcion "Visitados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        #Y elijo la ruta "1222654"
        Cuando selecciono "Visitados"
        Entonces valido la pantalla de "Visitados"

    Escenario: Validacion de opcion "Anulados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        #Y elijo la ruta "1222654"
        Cuando selecciono "Anulados"
        Entonces valido la pantalla de "Anulados
