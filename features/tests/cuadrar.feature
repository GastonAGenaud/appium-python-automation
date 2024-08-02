# language: es
@cuadrar
Característica: Cuadrar

    Escenario: Validación de la pantalla "Vuelta finalizada"
        Dado Reseteo la app
        Y el usuario ingresa el correo electronico "simple"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y selecciono la vuelta "Vuelta 1"
        Y hago click en el boton "Iniciar vuelta"
        Y elijo la ruta "LIKE EAT FOODS SPA"
        Y selecciono la factura con numero "404145535"
        Y hago click en el boton "Aceptar"
        Y hago click en el boton "Confirmar"
        Y selecciono la segunda factura con numero "404145535"
        Y hago click en el boton "Aceptar"
        Y hago click en el boton "Confirmar"
        Entonces valido que las facturas fueron entregadas
        Cuando hago click en el boton "Confirmar"
        Entonces valido el Total esperado "$ 1.885.008"
        Y valido el Total recaudado "$ 1.885.008"
        Y valido el Total rebajado "$0"
        Y valido que por Transferencia el monto abonado es "0"
        Y valido que por Efectivo el monto abonado es "$ 1.885.008"
        Y valido que por Cheque el monto abonado es "$0"
        Y valido que por Credito el monto abonado es "$0"
        Cuando hago click en el boton "Cerrar vuelta 1"
        Y hago click en el boton "Confirmar cierre de vueltas"
        Entonces valido que se muestre el mensaje "¡Vuelta cerrada!"


    @regresion
    Escenario: Validación del texto de la fecha de ruta
        Dado Reseteo la app
        Y Ingreso con el conductor a la aplicacion
        Cuando selecciono la vuelta "Vuelta 1"
        Entonces se valida el texto de la fecha

    @regresion
    Escenario: Validación del texto "25 clientes"
        Dado Ingreso con el conductor a la aplicacion
        Entonces se valida el texto "25 clientes"

    @modalComenzarRuta
    Escenario: Validacion del texto "Entregada"
        Dado Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Iniciar vuelta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "812345672"
        Y hago click en el boton "Aceptar"
        Y selecciono el metodo de pago "Transferencia"
        Y hago click en el boton "Confirmar"
        Y hago click en el boton "Confirmar"
        Entonces valido el texto "Entregado"

