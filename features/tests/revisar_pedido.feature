# language: es

Característica: Revisar pedido

    Esquema del escenario: Validacion de visualizacion de ruta de pedido
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Cuando elijo la ruta "<idRuta>"
        Entonces se valida que la visualizacion de pedido para la ruta "<idRuta>" sea correcta

        Ejemplos:
            | idRuta   |
            | Renca    |
            | Pudahuel |

    #Esquema del escenario: Validacion de visualizacion del nombre <idNombre> en el pedido
    #    Dado ingreso el correo electronico "<correoElectronico>"
    #    Y ingreso la contrasena "<contrasena>"
    #    Y hago click en el boton "Ingresar"
    #    Cuando elijo el nombre "<idNombre>"
    #    Entonces se valida que la visualizacion de pedido para "<idNombre>" sea correcta

    #    Ejemplos:
    #        | correoElectronico | contrasena | idNombre        |
    #        | test@test.com      | test123 | Test            |
    #        | Jonathan           | test123 | Leandro Maronas |

    Esquema del escenario: Validacion de visualizacion de la cantidad de productos y el monto de transferencia
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        #Y elijo el nombre "Test"
        Y elijo la ruta "<idRuta>"
        #Cuando presiono el boton "Ver detalle"
        Entonces valido la visualizacion del monto de la transferencia "<precio>" y de los productos "<producto>"

        Ejemplos:
            | idRuta   | precio  | producto |
            | Pudahuel | $ 2.000 | 20       |

    Escenario: Validacion de opciones en el modal al presionar "Ver indicaciones en mapa"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        #Y elijo el nombre "Test"
        Cuando elijo la ruta "Pudahuel"
        #Cuando presiono el boton "Ver indicaciones en mapa"
        #Entonces valido que se muestre el modal de indicaciones en el mapa
        Y valido la presencia de la opcion "Google Maps"
        #Y valido la presencia de la opcion "Waze"

    Escenario: Validacion del contenido de la factura
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Y elijo la ruta "Pudahuel"
        Cuando selecciono la factura con numero "388717884"
        Entonces valido el producto "Coca Cola Zero 1.5 LT Pack 1"
        Y valido el precio unitario "$2.000"
        #Y valido el precio del pack "<precioPack>"
        Y valido el sector de botones de agregar y restar
        Y valido el precio final "$40.000"
        Y valido que el precio total sea de "$2.000"

    Escenario: Anular pedido de la factura
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Y elijo la ruta "Pudahuel"
        Cuando selecciono la factura con numero "388717884"
        Y hago click en el boton "Anular pedido"
        Entonces valido que se muestre una confirmacion de anulacion del pedido

    Escenario: Entregar pedido de la factura
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Y elijo la ruta "Pudahuel"
        Cuando selecciono la factura con numero "388717884"
        Y hago click en el boton "Entregar"
        Entonces valido que se muestre una confirmacion de entrega del pedido