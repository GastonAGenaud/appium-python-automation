# language: es
@anular_pedido
Característica: Anular pedido

  @porqueretornar
  Escenario: Validación de presionar el boton "Anular pedido"
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono el boton "Retornar pedido"
    Entonces valido que se haya abierto la pantalla de selección de motivo de anulación

  Escenario: Validación de motivo de anulación
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono el boton "Retornar pedido"
    Cuando visualizo la pantalla de selección de motivo de anulacion
    Entonces valido la presencia de los siguientes motivos:
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

  @AnularPedido
  Escenario: Validación de pantalla de selección de motivo de anulación
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono el boton "Retornar pedido"
    Cuando visualizo la pantalla de selección de motivo de anulacion
    Entonces valido la presencia de los siguientes motivos:
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
    Cuando selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Entonces verifico que se envíe el motivo seleccionado correctamente

  @rutaAnterior
  Escenario: Validación del sector "Retornados"
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono el boton "Retornar pedido"
    Y selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Y hago click en el boton "Retornados"
    Entonces valido que la ruta utilizada anteriormente esté presente

  @anularPedidoFactura
  Escenario: Validación de retornar pedido de factura
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y selecciono el boton "Retornar pedido"
    Y selecciono "Sobre stock"
    Y hago clic en el botón "Confirmar"
    Entonces verifico la validacion del retorno de la factura

  @retomarPedido
  Escenario: Validación de la pantalla de retomar pedidos
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145531"
    Y selecciono el boton "Retornar pedido"
    Y selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Y selecciono la segunda factura factura con numero "404145531"
    Y selecciono el boton "Retornar pedido"
    Y selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Y selecciono el boton "Retornar pedido"
    Y selecciono "Sobre stock"
    Y hago click en el boton "Confirmar"
    Y hago click en el boton "Retornados"
    Entonces Valido la pantalla de retomar pedidos


  #Escenario: Validación del boton "Ver detalle" en la pantalla de retomar pedidos
   # Dado hago click en el boton "Ingresar"
   # Y visualizo la pantalla de retomar pedidos
   # Y valido la presencia del boton "Ver detalle"
   # Cuando hago click en el boton "Ver detalle"
   # Entonces verifico que se redireccione
