# language: es

Característica: Cuadrar

    Escenario: Validación de la pantalla "Vuelta finalizada"
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        #Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145531"
        Y visualizo la pantalla "Ruta finalizada"
        Entonces valido que el producto "Ades de Naranja 700 ML Pack 6" esté presente
        Y valido el total como "$3.400.200"
        Y valido el total de transferencia como "$1.700.000"
        Y valido el total de efectivo como "$1.000.000"
        Y valido el total de cheque como "$400.200"
        Y valido el total de crédito como "$1.600.200"
        Y valido el total rebajado como "$90.800"
        Y valido la presencia del botón "Cerrar transporte"
        Y valido que se muestre el mensaje "Transporte listo"

  @regresion
  Escenario: Validación del texto "RUTA 20 MAYO"
    Dado el usuario ingresa el correo electronico "user_tests"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y cierro el cuadro de texto
    Entonces se valida el texto "RUTA 20 MAYO"

  @regresion
  Escenario: Validación del texto "25 clientes"
    Dado el usuario ingresa el correo electronico "user_tests"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y cierro el cuadro de texto
    Entonces se valida el texto "25 clientes"

  @modalComenzarRuta
  Escenario: Validacion del modal de ruta comenzada
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Entonces valido el modal de ruta comenzada

  @modalComenzarRuta
  Escenario: Validacion del texto "Entregada"
    Dado el usuario ingresa el correo electronico "conductor-01"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y cierro el cuadro de texto
    Y hago click en el boton "Comenzar ruta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "404145544"
    Y hago click en el boton "entregar"
    Y hago click en el boton "Confirmar"
    Entonces valido el texto "Entregada"

