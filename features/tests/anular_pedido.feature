# language: es

Característica: Anular pedido


  Esquema del escenario: Validación de presionar el boton "Anular pedido"
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contrasena "<contrasena>"
    Y hago click en el boton "Ingresar"
    Cuando visualizo la factura con número "<numeroFactura>"
    Y hago click en el boton "Anular pedido"
    Entonces valido que se haya abierto la pantalla de selección de motivo de anulación

    Ejemplos:
      | correoElectronico | contrasena | numeroFactura |
      | test@test.com     | test123    | 3942342       |

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
    Y selecciono "Sobre stock"
    Y valido la presencia del boton "Confirmar"
    Cuando hago click en el boton "Confirmar"
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


  Esquema del escenario: Validación de la pantalla de retomar pedidos
    Dado hago click en el boton "Ingresar"
    Y visualizo la pantalla de retomar pedidos
    Y valido que la ruta del pedido sea "Felix de Amesti 920"
    Y valido la presencia del boton "Retomar pedido"
    Y hago click en el boton "Retomar pedido"
    Entonces verifico que se redireccione a la pantalla de detalles del pedido
    Y verifico que se muestre correctamente el pedido a retomar

    Ejemplos:
      | correoElectronico | contrasena |
      | test@test.com     | test123    |

  Escenario: Validación del boton "Ver detalle" en la pantalla de retomar pedidos
    Dado hago click en el boton "Ingresar"
    Y visualizo la pantalla de retomar pedidos
    Y valido la presencia del boton "Ver detalle"
    Cuando hago click en el boton "Ver detalle"
    Entonces verifico que se redireccione
