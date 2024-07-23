# language: es
@revisar_pedido
Característica: Revisar pedido

  Escenario: Validacion de visualizacion de ruta de pedido
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Entonces se valida que la visualizacion de pedido para la ruta "El Deseo SPA" sea correcta

  Escenario: Validacion de visualizacion de la cantidad de productos y el monto de transferencia
    Dado Ingreso con el conductor a la aplicacion
    Entonces valido la visualizacion del monto de la transferencia
    Y valido la visualizacion de la cantidad de los productos

  Escenario: Validacion de opciones en el modal al presionar "Ver indicaciones en mapa"
    Dado Ingreso con el conductor a la aplicacion
    Entonces valido la presencia de la opcion "Google Maps"

  Esquema del escenario: Validacion del contenido de la factura
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
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
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en el boton "Retornar factura"
        #Entonces valido que se muestre una confirmacion de anulacion del pedido

  Escenario: Validacion del precio total del pedido
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Entonces valido que este correcta la suma del precio de los productos

  Escenario: Entregar pedido de la factura
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en el boton "entregar"
    #Y selecciono el metodo que te van a pagar "efectivo"
    Entonces valido el texto "No hay productos rebajados"
    Cuando hago click en el boton "Confirmar"
    Entonces valido el texto "Entregada"

  #No tiene nota de credito 25.000
#  Escenario: Valido la Nota de Credito
#    Dado Reseteo la app
#    Y el usuario ingresa el correo electronico "simple"
#    Y el usuario ingresa una contraseña
#    Cuando hago click en el boton "Iniciar sesion"
#    Y selecciono la vuelta "Vuelta 1"
#    Y hago click en el boton "Iniciar vuelta"
#    Y elijo la ruta "Erbi"
#    Entonces valido que la nota de credito sea "- $ 25.000"

  Esquema del escenario: Valido la seccion de metodo de pago desde la factura
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en la opcion "metodo de pago"
    Entonces valido el texto "¿Con qué te van a pagar?"
    Y valido que el precio total sea de "$ 508.147"
    Y valido que sea visible el metodo de pago "<metodo>"

    Ejemplos:
      | metodo                       |
      | Transferencia                |
      | Efectivo                     |
      | Con más de un método de pago |

  Escenario: Valido la seccion de metodo de pago "Transferencia"
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en la opcion "metodo de pago"
    Y selecciono el metodo de pago "Transferencia"
    Y hago click en el boton "Confirmar"
    Entonces valido el mensaje "Metodo de pago editado"

  Escenario: Valido la seccion de metodo de pago "Efectivo"
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en la opcion "metodo de pago"
    Y selecciono el metodo de pago "Efectivo"
    Y hago click en el boton "Confirmar"
    Entonces valido el mensaje "Metodo de pago editado"

  Escenario: Valido la seccion de metodo de pago "Con mas de un metodo de pago"
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en la opcion "método de pago"
    Y selecciono el metodo de pago "Con más de un método de pago"
    Y hago click en el check "Efectivo"
    Y hago click en el check "Transferencia"
    Y Ingreso los montos en efectivo y transferencia
    Y hago click en el boton "Confirmar"
    Entonces valido el mensaje "Metodo de pago editado"

  Escenario: Valido el texto que se muestra en el sector de pago con Cheque
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en la opcion "método de pago"
    Y selecciono el metodo de pago "Con más de un método de pago"
    Entonces valido el mensaje que se muestra en el sector Cheque
