# language: es
@modificar_recorrido
Característica: Modificar recorrido sugerido

    @regresion
    Escenario: Validacion de la pantalla Comenzar ruta
        Dado Ingreso con el conductor a la aplicacion
        Entonces valido que se visualice el boton "Comenzar ruta"

    @regresion
    Escenario: Validacion del boton "Comenzar ruta"
        Dado Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Iniciar vuelta"
        Entonces se valida que el boton "Comenzar ruta" haya sido seleccionado correctamente

    @regresion
    Esquema del escenario: Validacion de la ruta
        Dado Ingreso con el conductor a la aplicacion
        Entonces valido que sea visible la "<caracteristica>" con el "<valor>" del pedido

        Ejemplos:
            | caracteristica | valor                  |
            | Local          | EL DESEO SPA           |
            | Direccion      | AVDA ANDRES BELLO 2447 |
            | Producto       | 16                     |
            | Transferencia  | $866.455               |

    @regresion
    Escenario: Validacion de seleccion de ruta
        Dado Ingreso con el conductor a la aplicacion
        Cuando elijo la ruta "El Deseo SPA"
        Entonces se valida que la ruta "El Deseo SPA" este seleccionada

    @regresion
    Esquema del escenario: Validacion del desplegable "Ordenar por"
        Dado Reseteo la app
        Y Ingreso con el conductor a la aplicacion
        Cuando hago click en el desplegable
        Entonces valido que sea visible la opcion "<opcion>"

        Ejemplos:
            | opcion          |
            | Mas productos   |
            | Menos productos |
            | Ruta sugerida   |

    @regresion
    Escenario: Validacion de la modificacion de la ruta por boton (hacia arriba)
        Dado Reseteo la app
        Y Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Modificar"
        Y hago click en el boton "Entendido"
        Y hago click en el boton "Desplegar"
        Y hago click en el boton "Mover hacia arriba"
        Entonces valido el mensaje que el cliente modifico su ubicacion hacia arriba en la lista

    @regresion
    Escenario: Validacion de la modificacion de la ruta por boton (hacia abajo)
        Dado Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Desplegar"
        Y hago click en el boton "Mover a lo más abajo"
        Entonces valido el mensaje que el cliente modifico su ubicacion hacia mas abajo en la lista

    @regresion
    Escenario: Validacion de opcion "Entregados"
        Dado Ingreso con el conductor a la aplicacion
        Cuando selecciono "Entregados"
        Entonces valido la pantalla de "Entregados"

    @regresion
    Escenario: Validacion de opcion "Retornados"
        Dado Ingreso con el conductor a la aplicacion
        Cuando selecciono "Retornados"
        Entonces valido la pantalla de "Retornados"
