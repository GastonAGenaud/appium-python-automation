Feature: Revisar pedido

    Background:
        Given Voy a la pantalla de inicio de sesion

    Scenario Outline: Validacion de visualizacion de ruta de pedido <idRuta>
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "<idRuta>"
        Then se valida que la visualizacion de pedido para la ruta "<idRuta>" sea correcta

        Examples:
            | correoElectronico | contraseña | idRuta              |
            | test@test.com     | test123    | Felix de Amesti 920 |
            | Jonathan          | test123    | Padre Tadeo 957     |

    Scenario Outline: Validacion de visualizacion del nombre <idNombre> en el pedido
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo el nombre "<idNombre>"
        Then se valida que la visualizacion de pedido para "<idNombre>" sea correcta

        Examples:
            | correoElectronico | contraseña | idNombre        |
            | test@test.com     | test123    | Test            |
            | Jonathan          | test123    | Leandro Maroñas |

    Scenario Outline: Validacion de visualizacion de la cantidad de productos <producto> y el monto de transferencia <precio>
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo el nombre "Test"
        When elijo la ruta "<idRuta>"
        And presiono el boton "Ver detalle"
        Then valido la visualizacion del monto de la transferencia "<precio>" y de los productos "<producto>"

        Examples:
            | correoElectronico | contraseña | idRuta              | precio   | producto     |
            | test@test.com     | test123    | Felix de Amesti 920 | $100.000 | Productos 15 |

    Scenario Outline: Validacion de opciones en el modal al presionar "Ver indicaciones en mapa"
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo el nombre "Test"
        When elijo la ruta "Felix de Amesti 920"
        And presiono el boton "Ver indicaciones en mapa"
        Then valido que se muestre el modal de indicaciones en el mapa
        And valido la presencia de la opcion "Google Maps"
        And valido la presencia de la opcion "Waze"

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion del contenido de la factura
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo el nombre "Test"
        When visualizo la factura con numero "<numeroFactura>"
        Then valido el producto "<producto>"
        And valido el precio unitario "<precioUnitario>"
        And valido el precio del pack "<precioPack>"
        And valido el sector de botones de agregar y restar
        And valido el precio final "<precioFinal>"
        And valido que el total sea de $450.000

        Examples:
            | correoElectronico | contraseña | numeroFactura | producto                   | precioUnitario | precioPack | precioFinal |
            | test@test.com     | test123    | 3942342       | Ades Naranja 700 ML Pack 6 | $1.000         | $1.800     | $5.400      |
            | test@test.com     | test123    | 3942343       | Ades Durazno 700 ML Pack 6 | $1.000         | $1.800     | $1.800      |
            | test@test.com     | test123    | 3942344       | Ades Pera 700 ML Pack 6    | $1.000         | $1.800     | $1.800      |
            | test@test.com     | test123    | 3942344       | Ades Mango 700 ML Pack 6   | $1.000         | $1.800     | $1.800      |

    Scenario: Anular pedido de la factura
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo el nombre "Test"
        When visualizo la factura con numero "3942342"
        And presiono el boton "Anular pedido"
        Then valido que se muestre una confirmacion de anulacion del pedido

    Scenario: Entregar pedido de la factura
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo el nombre "Test"
        When visualizo la factura con numero "3942342"
        And presiono el boton "Entregar"
        Then valido que se muestre una confirmacion de entrega del pedido