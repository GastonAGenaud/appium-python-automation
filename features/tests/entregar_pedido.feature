# language: es

Característica: Entregar pedido

    Escenario: Validación de la pantalla "Entregar pedidos" en el sector "Rebajados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Cuando elijo la ruta "Pudahuel"
        Y selecciono la factura con numero "388717884"
        Y selecciono para rebajar el pedido
        Y hago click en el boton "Entregar"
        Y selecciono "Rebajados"
        Entonces valido el producto "Coca Cola Zero 1.5 LT Pack 1"
        Y valido el total de la factura como "$ 38.000"
        Y valido el total rebajado como "$ 2.000"
        Y hago click en el boton "Confirmar"
        Y valido mensaje de entrega completada



    Escenario: Validación de la pantalla "Entregar pedidos" en el sector "Entregados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contrasena
        Y hago click en el boton "Ingresar"
        Cuando elijo la ruta "Pudahuel"
        Y selecciono la factura con numero "388717884"
        Y selecciono para rebajar el pedido
        Y hago click en el boton "Entregar"
        Entonces valido el producto "Coca Cola Zero 1.5 LT Pack 1"
        Y valido el total de la factura como "$ 38.000"
        Y valido el total rebajado como "$ 2.000"
        Y hago click en el boton "Confirmar"
        Y valido mensaje de entrega completada


