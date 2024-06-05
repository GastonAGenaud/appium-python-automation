# language: es
@rebajarPedido
Característica: Rebajar Pedido

  Escenario: Rebajar precio de un producto y seleccionar motivo de anulacion en la factura
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y selecciono para rebajar el pedido
    Y selecciono el boton "Retornar pedido"
    Y selecciono "Sobre stock"
    Cuando hago click en el boton "Confirmar"
    Entonces verifico pantalla del producto rebajado

  Escenario: Validacion de pantalla de seleccion de motivo de rebaja
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono el boton "Retornar pedido"
    Cuando visualizo la pantalla de selección de motivo de anulacion
    Entonces valido la presencia de los motivos de anulacion:
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
      | Capacidad cliente               |
      | Fuera de ruta                   |
      | Producto deteriorado            |
      | Sin dinero                      |
      | Cliente anula pedido            |
      | Diferencia de condicion de pago |
      | Envase                          |
      | Capacidad cliente               |
      | Diferencia en condición de pago |
      | Falta de producto               |
      | Horario inadecuado              |
      | Entrega atrasada                |
      | Exceso de clientes              |
