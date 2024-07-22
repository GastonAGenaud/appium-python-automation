# language: es
@anular_pedido
Característica: Anular pedido

  @porqueretornar
  Escenario: Validación de presionar el boton "Anular pedido"
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y hago click en el boton "Retornar todo"
    Entonces valido que se haya abierto la pantalla de selección de motivo de anulación

  Escenario: Validación de motivo de anulación
    Dado Ingreso con el conductor a la aplicacion
    Cuando visualizo la pantalla de selección de motivo de anulacion
    Entonces valido la presencia de los motivos de anulacion:
      | motivo                          |
      | Duplicado/Mal digitado          |
      | Local No Encontrado             |
      | Ausencia Encargado Local        |
      | Sobre stock                     |
      | Problema de fecha               |
      | Diferencia en condición de pago |
      | Falta de producto               |
      | Sin orden de compra             |
      | Dificultad en ruta              |
      | Envase                          |
      | Capacidad cliente               |
      | Horario inadecuado              |
      | Entrega atrasada                |
      | Exceso de clientes              |

  @AnularPedido
  Escenario: Validación de pantalla de selección de motivo de anulación
    Dado Ingreso con el conductor a la aplicacion
    Cuando visualizo la pantalla de selección de motivo de anulacion
      | motivo                          |
      | Duplicado/Mal digitado          |
      | Local No Encontrado             |
      | Ausencia Encargado Local        |
      | Sobre stock                     |
      | Problema de fecha               |
      | Diferencia de condición de pago |
      | Falta de producto               |
      | Sin orden de compra             |
      | Dificultad en ruta              |
      | Envase                          |
      | Capacidad cliente               |
      | Horario inadecuado              |
      | Entrega atrasada                |
      | Exceso de clientes              |
    Cuando selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Entonces verifico que se envíe el motivo seleccionado correctamente

  @rutaAnterior
  Escenario: Validación del sector "Retornados"
    Dado Ingreso con el conductor a la aplicacion
    Cuando selecciono "Retornados"
    Entonces valido que la ruta utilizada anteriormente esté presente

  @anularPedidoFactura
  Escenario: Validación de retornar pedido de factura
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en el boton "Retornar factura"
    Y selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Entonces verifico la validacion del retorno de la factura

  @retomarPedido
  Escenario: Validación de la pantalla de retomar pedidos
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y hago click en el boton "Retornar factura"
    Y selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Y selecciono la segunda factura con numero "404145531"
    Y hago click en el boton "Retornar factura"
    Y selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Y hago click en el boton "Retornar todo"
    Y selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Y selecciono "Retornados"
    Entonces Valido la pantalla de retomar pedidos
