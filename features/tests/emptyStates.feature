# language: es

Característica: Estados Vacíos

  Antecedentes:
    Dado que voy a la pantalla de inicio de sesión

  Esquema del escenario: Validación de pantalla "Visitados"
    Y ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contraseña "<contraseña>"
    Y hago clic en el botón "Ingresar"
    Cuando selecciono "Visitados"
    Y valido el texto "Aun no visitas a ningun cliente"
    Entonces valido la pantalla de "Visitados"

    Ejemplos:
      | correoElectronico | contraseña |
      | test@test.com     | test123    |
      | Jonathan          | test123    |

  Esquema del escenario: Validación de pantalla "Anulados"
    Y ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contraseña "<contraseña>"
    Y hago clic en el botón "Ingresar"
    Cuando selecciono "Anulados"
    Y valido el texto "No has anulado pedidos"
    Y valido el texto "Presiona al cliente para anular un pedido completo"
    Entonces valido la pantalla de "Anulados"

    Ejemplos:
      | correoElectronico | contraseña |
      | test@test.com     | test123    |
      | Jonathan          | test123    |
