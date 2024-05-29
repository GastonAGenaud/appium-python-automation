# language: es
@entregar_pedido
Característica: Entregar pedido

    @regresion
    Escenario: Validación de la pantalla "Entregar pedidos" en el sector "Rebajados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145531"
        Y selecciono para rebajar el pedido
        Y hago click en el boton "entregar"
        Y selecciono "Rebajados"
        Entonces valido el producto "Coca Cola LT220cc"
        Y valido el total de la factura como "$ 872.818"
        Y valido el total rebajado como "$ 57.652"
        Y hago click en el boton Confirmar
        #Y valido mensaje de entrega completada

    @regresion
    Escenario: Validación de la pantalla "Entregar pedidos" en el sector "Entregados"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145531"
        Y selecciono para rebajar el pedido
        Y hago click en el boton "entregar"
        Entonces valido el producto "Coca Cola LT220cc"
        Y valido el total de la factura como "$ 872.818"
        Y valido el total rebajado como "$ 57.652"
        Y hago click en el boton Confirmar
        #Y valido mensaje de entrega completada
