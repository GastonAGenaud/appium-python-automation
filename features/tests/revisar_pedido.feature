# language: es

Característica: Revisar pedido

    @regresion
    Escenario: Validacion de visualizacion de ruta de pedido
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Entonces se valida que la visualizacion de pedido para la ruta "El Deseo SPA" sea correcta

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

    @regresion
    Escenario: Validacion de visualizacion de la cantidad de productos y el monto de transferencia
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y elijo el nombre "Test"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        #Cuando presiono el boton "Ver detalle"
        Entonces valido la visualizacion del monto de la transferencia
        Y valido la visualizacion de la cantidad de los productos

    @regresion
    Escenario: Validacion de opciones en el modal al presionar "Ver indicaciones en mapa"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y elijo el nombre "Test"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        #Cuando presiono el boton "Ver indicaciones en mapa"
        #Entonces valido que se muestre el modal de indicaciones en el mapa
        Entonces valido la presencia de la opcion "Google Maps"
        #Y valido la presencia de la opcion "Waze"

    @regresion
    Esquema del escenario: Validacion del contenido de la factura
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145544"
        Entonces valido el producto "<producto>"
        Y valido el precio unitario "<precioUnitario>"
        Y valido la cantidad de pack pedidos "<cantidadPack>"
        Y valido el sector de botones de agregar y restar
        Y valido el precio final "<precioTotal>"
        Y valido que el precio total sea de "$ 930.470"

        Ejemplos:
            | producto                   | precioUnitario | cantidadPack | precioTotal |
            | Coca Cola LT220cc          | $ 57.652       | 4            | $ 230.608   |
            | Fanta MidCal PT250cc       | $ 46.913       | 5            | $ 234.565   |
            | Fanta MidCal Express 237cc | $ 66.471       | 7            | $ 465.297   |

    @regresion
    Escenario: Anular pedido de la factura
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        #Y selecciono la factura con numero "404145544"
        Y hago click en el boton "Retornar pedido"
        #Entonces valido que se muestre una confirmacion de anulacion del pedido

    @regresion
    Escenario: Entregar pedido de la factura
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145544"
        Y hago click en el boton "Entregar"
        Y hago click en el boton "Confirmar"
        #Entonces valido mensaje de entrega completada

    @regresion
    Escenario: Validacion del precio total del pedido
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145544"
        Entonces valido que este correcta la suma del precio de los productos

    Escenario: Validacion del mensaje al rebajar producto
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145544"
        Entonces debería ver el mensaje "El producto ha sido rebajado exitosamente a 50.00"


