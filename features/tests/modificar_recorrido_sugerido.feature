# language: es

Característica: Modificar recorrido sugerido

    @regresion
    Escenario: Validacion de la pantalla Comenzar ruta
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Entonces valido que se visualice el boton "Comenzar ruta"

    @regresion
    Esquema del escenario: Validacion de la ruta
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Entonces valido que sea visible la "<caracteristica>" con el "<valor>" del pedido

        Ejemplos:
            | caracteristica | valor                  |
            | Local          | EL DESEO SPA           |
            | Direccion      | AVDA ANDRES BELLO 2447 |
            | Producto       | 16                     |
            | Transferencia  | $930.470               |

    @regresion
    Escenario: Validacion de seleccion de ruta
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Entonces se valida que la ruta "El Deseo SPA" este seleccionada

    @regresion
    Escenario: Validacion del boton "Comenzar ruta"
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y elijo la ruta "1222654"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Entonces se valida que el boton "Comenzar ruta" haya sido seleccionado correctamente

    @regresion
    Esquema del escenario: Validacion del desplegable "Ordenar por"
        Dado el usuario ingresa el correo electronico "conductor-01"
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
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Modificar"
        Entonces valido que el texto "<opcion>" de la pantalla de modificacion manual

        Ejemplos:
            | opcion           |
            | Modifica tu ruta |
            #| Presiona prolongadamente |
            | Entendido        |
            #| No volver a mostrar |

    #Escenario: Validacion de la modificacion de la ruta
        #Dado el usuario ingresa el correo electronico "conductor-01"
        #Y el usuario ingresa una contraseña
        #Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        #Y hago click en el boton "Modificar"
        #Y hago click en el boton "Entendido"
        #Y desplazo un cliente hacia una nueva posicion
        #Entonces valido el mensaje "Recorrido modificado"

    @regresion
    Escenario: Validacion de la modificacion de la ruta por boton (hacia arriba)
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Modificar"
        Y hago click en el boton "Entendido"
        Y hago click en el boton "Desplegar"
        Y hago click en el boton "Mover hacia arriba"
        Entonces valido el mensaje que el cliente modifico su ubicacion hacia arriba en la lista

    @regresion
    Escenario: Validacion de la modificacion de la ruta por boton (hacia abajo)
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Modificar"
        Y hago click en el boton "Entendido"
        Y hago click en el boton "Desplegar"
        Y hago click en el boton "Mover a lo más abajo"
        Entonces valido el mensaje que el cliente modifico su ubicacion hacia mas abajo en la lista


    @regresion
    Escenario: Validacion de opcion "Entregados"
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y selecciono "Entregados"
        Entonces valido la pantalla de "Entregados"

    @regresion
    Escenario: Validacion de opcion "Retornados"
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y selecciono "Retornados"
        Entonces valido la pantalla de "Retornados"
