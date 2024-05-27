# language: es

Característica: Revisar pedido

    Esquema del escenario: Validacion de visualizacion de ruta de pedido
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Y hago click en el boton "Ingresar"
        Cuando elijo la ruta "<idRuta>"
        Entonces se valida que la visualizacion de pedido para la ruta "<idRuta>" sea correcta

        Ejemplos:
            | idRuta   |
            | Renca    |
            | Pudahuel |

    Escenario: Validacion de visualizacion de la cantidad de productos y el monto de transferencia
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Ingresar"
        #Y elijo el nombre "Test"
        Y elijo la ruta "Pudahuel"
        #Cuando presiono el boton "Ver detalle"
        Entonces valido la visualizacion del monto de la transferencia
        Y valido la visualizacion de la cantidad de los productos

    Escenario: Validacion de opciones en el modal al presionar "Ver indicaciones en mapa"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Ingresar"
        #Y elijo el nombre "Test"
        Y elijo la ruta "Pudahuel"
        #Cuando presiono el boton "Ver indicaciones en mapa"
        #Entonces valido que se muestre el modal de indicaciones en el mapa
        Entonces valido la presencia de la opcion "Google Maps"
        #Y valido la presencia de la opcion "Waze"

    Escenario: Validacion del contenido de la factura
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "Pudahuel"
        Y selecciono la factura con numero "388717884"
        Entonces valido el producto "Coca Cola Zero 1.5 LT Pack 1"
        Y valido el precio unitario "$2.000"
        #Y valido el precio del pack "<precioPack>"
        Y valido el sector de botones de agregar y restar
        Y valido el precio final "$40.000"
        Y valido que el precio total sea de "$40.000"

    Escenario: Anular pedido de la factura
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "Pudahuel"
        Y selecciono la factura con numero "388717884"
        Y hago click en el boton "Anular pedido"
        Entonces valido que se muestre una confirmacion de anulacion del pedido

#    Escenario: Entregar pedido de la factura
#        Dado el usuario ingresa el correo electronico "user_tests"
#        Y el usuario ingresa una contraseña
#        Cuando hago click en el boton "Ingresar"
#        Y elijo la ruta "Pudahuel"
#        Y selecciono la factura con numero "388717884"
#        Y hago click en el boton "Entregar"
#        Y selecciono el botón de restar producto
#        Entonces valido mensaje de entrega completada