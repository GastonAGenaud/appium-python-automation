# language: es

Característica: Modificar recorrido sugerido

    Escenario: Validacion de la pantalla Comenzar ruta
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Entonces valido que se visualice el boton "Comenzar ruta"

    Esquema del escenario: Validacion de la ruta
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Entonces valido que sea visible la "<caracteristica>" con el "<valor>" del pedido

        Ejemplos:
            | caracteristica | valor                  |
            | Local          | EL DESEO SPA           |
            | Direccion      | AVDA ANDRES BELLO 2447 |
            | Producto       | 16                     |
            | Transferencia  | $930.470               |

    Escenario: Validacion de seleccion de ruta
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Entonces se valida que la ruta "El Deseo SPA" este seleccionada

    Escenario: Validacion del boton "Comenzar ruta"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y elijo la ruta "1222654"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Entonces se valida que el boton "Comenzar ruta" haya sido seleccionado correctamente

    Esquema del escenario: Validacion del desplegable "Ordenar por"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y hago click en el desplegable
        Entonces valido que sea visible la opcion "<opcion>"

        Ejemplos:
            | opcion          |
            | Mas productos   |
            | Menos productos |
            | Ruta sugerida   |

    Esquema del escenario: Validacion de pantalla de modificar manualmente
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Modificar"
        Entonces valido que el texto "<texto>" de la pantalla de modificacion manual

        Ejemplos:
            | texto     |
            #| Modifica tu ruta |
            #| Presiona prolongadamente |
            | Entendido |
            #| No volver a mostrar      |

    Escenario: Validacion de la modificacion de la ruta
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Modificar"
        Y hago click en el boton "Entendido"
        Y desplazo un cliente hacia una nueva posicion
        #Entonces valido el mensaje "Recorrido modificado"

    Escenario: Validacion de opcion "Entregados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y selecciono "Entregados"
        Entonces valido la pantalla de "Entregados"

    Escenario: Validacion de opcion "Retornados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y selecciono "Retornados"
        Entonces valido la pantalla de "Retornados"
