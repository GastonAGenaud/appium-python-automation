# language: es
@entregar_pedido
Característica: Entregar pedido

  @regresion
  Escenario: Validación de la pantalla "Entregar pedidos" en el sector "Retornados"
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
        #Y selecciono para rebajar el pedido
    Y hago click en el boton "entregar"
        #Y selecciono "Rebajados"
    Entonces valido el texto "No hay productos rebajados"
    Y hago click en el boton Confirmar
    Y valido el texto "Entregada"
        #Y valido mensaje de entrega completada

  @regresion
  Esquema del escenario: Validación de la pantalla "Entregar pedidos" en el sector "Entregados"
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
        #Y selecciono para rebajar el pedido
    Y hago click en el boton "entregar"
    Y selecciono el sector "Entregados"
    Entonces valido el producto "<producto>"
    Y valido el precio unitario "<precioUnitario>"
    Y valido que el precio total sea de "$ 508.147"
    Y hago click en el boton Confirmar
    Y valido el texto "Entregada"
        #Y valido mensaje de entrega completada

    Ejemplos:
      | producto                             | precioUnitario |
      | Sprite MidCal PT250cc x6             | $65.064        |
      | Fanta MidCal Express 237cc x 24      | $66.210        |
      | Benedictino S/G PT6.5 x 2 Cilindrico | $376.873       |


  Escenario: Valido la entrega de un pedido
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en el boton "entregar"
    Y hago click en el boton "Confirmar"
    Y selecciono la segunda factura factura con numero "404145531"
    Y hago click en el boton "entregar"
    Y hago click en el boton "Confirmar"
    Entonces valido que las facturas fueron entregadas
    Cuando hago click en el boton "Confirmar"
    Entonces valido el icono de la pantalla "Entrega impecable"
    Y valido el texto "Entrega impecable"
    Y valido el texto "¡Felicitaciones! Has entregado el pedido sin rebajas. Que siga la buena racha."
    Y valido el botón "Volver a mi ruta"

  Escenario: Valido que un pedido entregado este en el sector "Entregados"
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en el boton "entregar"
    Y hago click en el boton "Confirmar"
    Y selecciono la segunda factura factura con numero "404145531"
    Y hago click en el boton "entregar"
    Y hago click en el boton "Confirmar"
    Entonces valido que las facturas fueron entregadas
    Cuando hago click en el boton "Confirmar"
    Y hago click en el boton "Volver a mi ruta"
    Y selecciono "Entregados"
    Entonces Valido el pedido entregado correctamente