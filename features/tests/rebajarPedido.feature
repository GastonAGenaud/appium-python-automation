# language: es

Característica: Rebajar Pedido

    Esquema del escenario: Rebajar precio de un producto y seleccionar motivo de anulacion en la factura
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Cuando hago click en el boton "Ingresar"
        Y elijo el nombre "Test"
        Y visualizo la factura con numero "<numeroFactura>"
        Y hago click en el boton "-" para rebajar el precio del producto "<producto>"
        Y selecciono la opcion "<motivoAnulacion>" como motivo de anulacion
        Entonces valido que el precio final se haya ajustado correctamente
        Y valido que el motivo de anulacion se haya seleccionado correctamente

        Ejemplos:
            | correoElectronico | contrasena | numeroFactura | producto                   | motivoAnulacion        |
            | test@test.com     | test123    | 3942342       | Ades Naranja 700 ML Pack 6 | Duplicado/Mal digitado |

    Esquema del escenario: Validacion de pantalla de seleccion de motivo de rebaja
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Cuando hago click en el boton "Ingresar"
        Y elijo el nombre "Test"
        Y visualizo la pantalla de seleccion de motivo de rebaja
        Entonces valido la presencia de los siguientes motivos:
            | Producto deteriorado            |
            | Sin Dinero                      |
            | Sobre stock                     |
            | Diferencia en condicion de pago |
            | Problema de fecha (producto)    |
            | Duplicado/Mal digitado          |
            | Envase                          |
            | Falta de producto               |
            | Capacidad cliente               |
            | Diferencia de precio            |
        Y valido la presencia del boton "Enviar motivo"

        Ejemplos:
            | correoElectronico | contrasena |
            | test@test.com     | test123    |
