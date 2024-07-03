# language: es
@entregar_pedido
Característica: Entregar pedido

    @regresion
    Escenario: Validación de la pantalla "Entregar pedidos" en el sector "Retornados"
        Dado Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145531"
        Y hago click en el boton "entregar"
        Y selecciono el metodo que te van a pagar "efectivo"
        Y hago click en el boton "Confirmar"
        Entonces valido el texto "No hay productos rebajados"

    @regresion
    Esquema del escenario: Validación de la pantalla "Entregar pedidos" en el sector "Entregados"
        Dado Ingreso con el conductor a la aplicacion
        Cuando selecciono pestaña de "Entregados"
        Entonces valido el producto "<producto>"
        Y valido el precio unitario "<precioUnitario>"
        Y valido que el precio total sea de "$ 508.147"

        Ejemplos:
            | producto                             | precioUnitario |
            | Sprite MidCal PT250cc x6             | $65.064        |
            | Fanta MidCal Express 237cc x 24      | $66.210        |
            | Benedictino S/G PT6.5 x 2 Cilindrico | $376.873       |
