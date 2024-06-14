# language: es
@revisar_pedido
Característica: Revisar pedido


  Escenario: Validacion de visualizacion de ruta de pedido
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Entonces se valida que la visualizacion de pedido para la ruta "El Deseo SPA" sea correcta

    #Escenario: Validacion de visualizacion del nombre <idNombre> en el pedido
    #    Dado ingreso el correo electronico "<correoElectronico>"
    #    Y ingreso la contrasena "<contrasena>"
    #    Y hago click en el boton "Ingresar"
    #    Cuando elijo el nombre "<idNombre>"
    #    Entonces se valida que la visualizacion de pedido para "<idNombre>" sea correcta

  Escenario: Validacion de visualizacion de la cantidad de productos y el monto de transferencia
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y elijo el nombre "Test"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
        #Cuando presiono el boton "Ver detalle"
    Entonces valido la visualizacion del monto de la transferencia
    Y valido la visualizacion de la cantidad de los productos

  Escenario: Validacion de opciones en el modal al presionar "Ver indicaciones en mapa"
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y elijo el nombre "Test"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
        #Cuando presiono el boton "Ver indicaciones en mapa"
        #Entonces valido que se muestre el modal de indicaciones en el mapa
    Entonces valido la presencia de la opcion "Google Maps"
        #Y valido la presencia de la opcion "Waze"


  Esquema del escenario: Validacion del contenido de la factura
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Entonces valido el producto "<producto>"
    Y valido el precio unitario "<precioUnitario>" en la factura
    Y valido la cantidad de pack pedidos "<cantidadPack>"
    Y valido el sector de botones de agregar y restar
    Y valido el precio final "<precioTotal>"
    Y valido que el precio total sea de "$ 508.147"

    Ejemplos:
      | producto                             | precioUnitario | cantidadPack | precioTotal |
      | Sprite MidCal PT250cc x6             | $ 65.064       | 1            | $ 65.064    |
      | Fanta MidCal Express 237cc x 24      | $ 33.105       | 2            | $ 66.210    |
      | Benedictino S/G PT6.5 x 2 Cilindrico | $ 53.839       | 7            | $ 376.873   |


  Escenario: Anular pedido de la factura
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
        #Y selecciono la factura con numero "404145531"
    Y hago click en el boton "Retornar pedido"
        #Entonces valido que se muestre una confirmacion de anulacion del pedido


  Escenario: Entregar pedido de la factura
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en el boton "Entregar"
    Y hago click en el boton "Confirmar"
        #Entonces valido mensaje de entrega completada


  Escenario: Validacion del precio total del pedido
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Entonces valido que este correcta la suma del precio de los productos

  Escenario: Valido la Nota de Credito
    Dado el usuario ingresa el correo electronico "simple"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "Erbi"
    Entonces valido que la nota de credito sea "- $ 25.000"

#  Escenario: Validacion del mensaje al rebajar producto
#    Dado el usuario ingresa el correo electronico "user_tests"
#    Y el usuario ingresa una contraseña
#    Cuando hago click en el boton "Iniciar sesion"
#        #Y cierro el cuadro de texto
#    Y hago click en el boton "Comenzar ruta"
#    Y elijo la ruta "El Deseo SPA"
#    Y selecciono la factura con numero "404145531"
#    Entonces debería ver el mensaje "El producto ha sido rebajado exitosamente a 50.00"


