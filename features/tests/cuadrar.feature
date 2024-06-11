# language: es
@cuadrar
Característica: Cuadrar

    Escenario: Validación de la pantalla "Vuelta finalizada"
        Dado el usuario ingresa el correo electronico "simple"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "Erbi"
        Y selecciono la factura con numero "83908330"
        Y hago click en el boton "entregar"
        Y hago click en el boton "Confirmar"
        Y selecciono la factura con numero "8390812"
        Y hago click en el boton "entregar"
        Y hago click en el boton "Confirmar"
        Entonces valido que las facturas fueron entregadas
        Cuando hago click en el boton "Confirmar"
        Entonces valido el Total esperado "$811.371"
        Y valido el Total recaudado "$811.371"
        Y valido el Total rebajado "$0"
        Y valido que por Transferencia el monto abonado es "$0"
        Y valido que por Efectivo el monto abonado es "$0"
        Y valido que por Cheque el monto abonado es "$811.371"
        Y valido que por Credito el monto abonado es "$0"
        Cuando hago click en el boton "Cerrar transporte"
        Entonces valido que se muestre el mensaje "Transporte listo"


    @regresion
    Escenario: Validación del texto de la fecha de ruta
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Entonces se valida el texto de la fecha

    @regresion
    Escenario: Validación del texto "25 clientes"
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Entonces se valida el texto "25 clientes"

    #@modalComenzarRuta
    #Escenario: Validacion del modal de ruta comenzada
    #    Dado el usuario ingresa el correo electronico "conductor-01"
    #    Y el usuario ingresa una contraseña
    #    Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
    #    Y hago click en el boton "Comenzar ruta"
    #    Entonces valido el modal de ruta comenzada

    @modalComenzarRuta
    Escenario: Validacion del texto "Entregada"
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145531"
        Y hago click en el boton "entregar"
        Y hago click en el boton "Confirmar"
        Entonces valido el texto "Entregada"

