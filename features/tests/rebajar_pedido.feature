# language: es
@rebajar_pedido
Característica: Rebajar Pedido

  Escenario: Rebajar precio de un producto y seleccionar motivo de anulacion en la factura
    Dado Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y selecciono para rebajar el pedido
    Y hago click en el boton "Retornar factura"
    Y selecciono "Sobre stock"
    Cuando hago click en el boton "Confirmar"
    Entonces verifico pantalla del producto rebajado

  Escenario: Validacion de pantalla de seleccion de motivo de rebaja
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y hago click en el boton "Retornar todo"
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
      | Fuera de ruta                   |
      | Producto deteriorado            |
      | Sin dinero                      |
      | Cliente anula pedido            |
      | Envase                          |
      | Capacidad cliente               |
      | Horario inadecuado              |
      | Entrega atrasada                |
      | Exceso de clientes              |
