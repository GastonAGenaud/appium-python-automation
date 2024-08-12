# language: es
@entregar_pedido
Característica: Entregar pedido

  @regresion
  Escenario: Validación de la pantalla "Entregar pedidos" en el sector "Retornados"
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta 1"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "812345672"
    Y hago click en el boton "Aceptar"
    Y selecciono el metodo de pago "Transferencia"
    Y hago click en el boton "Confirmar"
    Entonces valido el texto "No hay productos rebajados"

  @regresion @entregadosValidacion
  Esquema del escenario: Validación de la pantalla "Entregar pedidos" en el sector "Entregados"
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta 1"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "812345672"
    Entonces valido el producto "<producto>"
    Y valido el precio unitario "<precioUnitario>"
    Y valido que el precio total sea de "$20.000"
    Ejemplos:
      | producto                         | precioUnitario |
      | Coca Cola Sin Azucar LT350cc x 6 | $ 1.000        |
      | Nordic Zero Ginger Ale PT3,0 x 6 | $ 1.000        |
      | Andina Nectar Damasco PT1,5 x 6  | $ 1.000        |


  @confirmarPedido
  Escenario: Valido la entrega de un pedido
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta 1"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "812345672"
    Y hago click en el boton "Aceptar"
    Y selecciono el metodo de pago "Transferencia"
    Y hago click en el boton "Confirmar"
    Y hago click en el boton "Confirmar modal"
    Y selecciono la segunda factura con numero "812345671"
    Y hago click en el boton "Aceptar"
    Entonces valido que las facturas fueron entregadas
    Cuando hago click en el boton "Confirmar"
    Entonces valido el icono de la pantalla "Entrega impecable"
    Y valido el texto "Entrega impecable"
    Y valido el texto "¡Felicitaciones! Has entregado el pedido sin rebajas. Que siga la buena racha."
    Cuando hago click en el boton "Confirmar"

  @confirmarPedido
  Escenario: Valido que un pedido entregado este en el sector "Entregados"
    Dado Ingreso con el conductor a la aplicacion
    Cuando selecciono "Entregados"
    Entonces Valido el pedido entregado correctamente