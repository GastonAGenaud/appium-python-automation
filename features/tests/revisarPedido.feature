# language: es

Característica: Revisar pedido

    Esquema del escenario: Validacion de visualizacion de ruta de pedido <idRuta>
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Y hago click en el boton "Ingresar"
        Cuando elijo la ruta "<idRuta>"
        Entonces se valida que la visualizacion de pedido para la ruta "<idRuta>" sea correcta

        Ejemplos:
            | correoElectronico | contrasena | idRuta              |
            | test@test.com     | test123    | Felix de Amesti 920 |
            | Jonathan          | test123    | Padre Tadeo 957     |

    Esquema del escenario: Validacion de visualizacion del nombre <idNombre> en el pedido
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Y hago click en el boton "Ingresar"
        Cuando elijo el nombre "<idNombre>"
        Entonces se valida que la visualizacion de pedido para "<idNombre>" sea correcta

        Ejemplos:
            | correoElectronico | contrasena | idNombre        |
            | test@test.com     | test123    | Test            |
            | Jonathan          | test123    | Leandro Maroñas |

    Esquema del escenario: Validacion de visualizacion de la cantidad de productos <producto> y el monto de transferencia <precio>
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Y hago click en el boton "Ingresar"
        Y elijo el nombre "Test"
        Y elijo la ruta "<idRuta>"
        Cuando presiono el boton "Ver detalle"
        Entonces valido la visualizacion del monto de la transferencia "<precio>" y de los productos "<producto>"

        Ejemplos:
            | correoElectronico | contrasena | idRuta              | precio   | producto     |
            | test@test.com     | test123    | Felix de Amesti 920 | $100.000 | Productos 15 |

    Esquema del escenario: Validacion de opciones en el modal al presionar "Ver indicaciones en mapa"
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Y hago click en el boton "Ingresar"
        Y elijo el nombre "Test"
        Y elijo la ruta "Felix de Amesti 920"
        Cuando presiono el boton "Ver indicaciones en mapa"
        Entonces valido que se muestre el modal de indicaciones en el mapa
        Y valido la presencia de la opcion "Google Maps"
        Y valido la presencia de la opcion "Waze"

        Ejemplos:
            | correoElectronico | contrasena |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion del contenido de la factura
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Y hago click en el boton "Ingresar"
        Cuando elijo el nombre "Test"
        Y visualizo la factura con numero "<numeroFactura>"
        Entonces valido el producto "<producto>"
        Y valido el precio unitario "<precioUnitario>"
        Y valido el precio del pack "<precioPack>"
        Y valido el sector de botones de agregar y restar
        Y valido el precio final "<precioFinal>"
        Y valido que el total sea de $450.000

        Ejemplos:
            | correoElectronico | contrasena | numeroFactura | producto                   | precioUnitario | precioPack | precioFinal |
            | test@test.com     | test123    | 3942342       | Ades Naranja 700 ML Pack 6 | $1.000         | $1.800     | $5.400      |
            | test@test.com     | test123    | 3942343       | Ades Durazno 700 ML Pack 6 | $1.000         | $1.800     | $1.800      |
            | test@test.com     | test123    | 3942344       | Ades Pera 700 ML Pack 6    | $1.000         | $1.800     | $1.800      |
            | test@test.com     | test123    | 3942344       | Ades Mango 700 ML Pack 6   | $1.000         | $1.800     | $1.800      |

    Escenario: Anular pedido de la factura
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Y hago click en el boton "Ingresar"
        Cuando elijo el nombre "Test"
        Y visualizo la factura con numero "3942342"
        Y presiono el boton "Anular pedido"
        Entonces valido que se muestre una confirmacion de anulacion del pedido

    Escenario: Entregar pedido de la factura
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contrasena "<contrasena>"
        Y hago click en el boton "Ingresar"
        Cuando elijo el nombre "Test"
        Y visualizo la factura con numero "3942342"
        Y presiono el boton "Entregar"
        Entonces valido que se muestre una confirmacion de entrega del pedido