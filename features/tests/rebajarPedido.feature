Feature: Rebajar Pedido

    Background:
        Given Voy a la pantalla de inicio de sesion

    Scenario Outline: Rebajar precio de un producto y seleccionar motivo de anulacion en la factura
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo el nombre "Test"
        When visualizo la factura con numero "<numeroFactura>"
        And hago click en el boton "-" para rebajar el precio del producto "<producto>"
        And selecciono la opcion "<motivoAnulacion>" como motivo de anulacion
        Then valido que el precio final se haya ajustado correctamente
        And valido que el motivo de anulacion se haya seleccionado correctamente

        Examples:
            | correoElectronico | contraseña | numeroFactura | producto                   | motivoAnulacion        |
            | test@test.com     | test123    | 3942342       | Ades Naranja 700 ML Pack 6 | Duplicado/Mal digitado |

    Scenario Outline: Validacion de pantalla de seleccion de motivo de rebaja
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo el nombre "Test"
        When visualizo la pantalla de seleccion de motivo de rebaja
        Then valido la presencia de los siguientes motivos:
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
        And valido la presencia del boton "Enviar motivo"

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
