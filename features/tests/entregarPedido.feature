# language: es

Característica: Entregar pedido

  Esquema del escenario: Validación de la pantalla "Entregar pedidos" en el sector "Rebajados"
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contrasena "<contrasena>"
    Y hago clic en el botón "Ingresar"
    Y elijo la ruta "Felix de Amesti 920"
    Cuando selecciono el botón "Comenzar ruta"
    Y visualizo la pantalla "Entregar pedidos" en el sector "Rebajados" con la factura "<numeroFactura>"
    Entonces valido que el producto "Ades de Naranja 700 ML Pack 6" esté presente
    Y valido el total de la factura como "<totalFactura>"
    Y valido el total rebajado como "<totalRebajado>"
    Y valido la presencia del botón "Confirmar"

    Ejemplos:
      | numeroFactura | totalFactura | totalRebajado |
      | 3942342       | $448.200     | $1.800        |

  Esquema del escenario: Validación de la pantalla "Entregar pedidos" en el sector "Entregados"
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contrasena "<contrasena>"
    Y hago clic en el botón "Ingresar"
    Y elijo la ruta "Felix de Amesti 920"
    Cuando selecciono el botón "Comenzar ruta"
    Y visualizo la pantalla "Entregar pedidos" en el sector "Entregados" con la factura "<numeroFactura>"
    Entonces valido que el producto "Ades de Naranja 700 ML Pack 6" esté presente
    Y valido el total de la factura como "<totalFactura>"
    Y valido el total rebajado como "<totalRebajado>"
    Y selecciono el botón "Confirmar"
    Entonces verifico que al confirmar se redirija a la pantalla de confirmación de entrega

    Ejemplos:
      | numeroFactura | totalFactura | totalRebajado |
      | 3942342       | $448.200     | $1.800        |
