# language: es

Característica: : Anular pedido

  Esquema del escenario: Validación de presionar el botón "Anular pedido"
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contraseña "<contraseña>"
    Y hago clic en el botón "Ingresar"
    Cuando visualizo la factura con número "<numeroFactura>"
    Y hago clic en el botón "Anular pedido"
    Entonces valido que se haya abierto la pantalla de selección de motivo de anulación

    Ejemplos:
    | correoElectronico | contraseña | numeroFactura |
    | test@test.com     | test123    | 3942342       |

  Esquema del escenario: Validación de pantalla de selección de motivo de anulación
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contraseña "<contraseña>"
    Y hago clic en el botón "Ingresar"
    Cuando visualizo la pantalla de selección de motivo de anulación
    Entonces valido la presencia de los siguientes motivos:
    | Sin dinero                      |
    | Cliente anula pedido            |
    | Diferencia en condición de pago |
    | Duplicado/Mal digitado          |
    | Sin orden de compra             |
    | Envase                          |
    | Ausencia del encargado          |
    | Producto deteriorado            |
    | Problema de fecha (producto)    |
    | Cerrado                         |
    | Sobre stock                     |
    | Problema de fecha               |
    | Dificultad en ruta              |
    | Falta de producto               |
    | Capacidad cliente               |
    | Horario inadecuado              |
    | Diferencia de precio            |
    | Entrega atrasada                |
    | Fuera de ruta                   |
    | Local no encontrado             |
    | Exceso de clientes              |
    Y valido la presencia del botón "Enviar motivo"
    Cuando hago clic en el botón "Enviar motivo"
    Entonces verifico que se envíe el motivo seleccionado correctamente

    Ejemplos:
    | correoElectronico | contraseña |
    | test@test.com     | test123    |
    | Jonathan          | test123    |

  Esquema del escenario: Validación del sector "Anulados"
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contraseña "<contraseña>"
    Y hago clic en el botón "Ingresar"
    Y elijo el nombre "Test"
    Cuando hago clic en el botón "Anulados" en el sector de selección de rutas
    Entonces valido que la ruta utilizada anteriormente "<idRuta>" esté presente
    Y valido la presencia del texto "Sobre stock"
    Y valido la presencia del botón "Comenzar ruta"

    Ejemplos:
    | correoElectronico | contraseña | idRuta              |
    | test@test.com     | test123    | Felix de Amesti 920 |

  Esquema del escenario: Validación de la pantalla de retomar pedidos
    Dado hago clic en el botón "Ingresar"
    Y visualizo la pantalla de retomar pedidos
    Entonces valido que la ruta del pedido sea "Felix de Amesti 920"
    Y valido la presencia del botón "Retomar pedido"
    Cuando hago clic en el botón "Retomar pedido"
    Entonces verifico que se redireccione a la pantalla de detalles del pedido
    Y verifico que se muestre correctamente el pedido a retomar

    Ejemplos:
    | correoElectronico | contraseña |
    | test@test.com     | test123    |

  Escenario: Validación del botón "Ver detalle" en la pantalla de retomar pedidos
    Dado hago clic en el botón "Ingresar"
    Y visualizo la pantalla de retomar pedidos
    Entonces valido la presencia del botón "Ver detalle"
    Cuando hago clic en el botón "Ver detalle"
    Entonces verifico que se redireccione
