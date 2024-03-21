# language: es

Característica: Cuadrar

  Esquema del escenario: Validación de la pantalla "Vuelta finalizada"
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contrasena "<contrasena>"
    Y hago clic en el botón "Ingresar"
    Y elijo la ruta "Felix de Amesti 920"
    Cuando selecciono el botón "Comenzar ruta"
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

    Ejemplos:
      | correoElectronico | contrasena |
      | test@test.com     | test123    |
      | Jonathan          | test123    |
