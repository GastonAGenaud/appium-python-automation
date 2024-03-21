# language: es

Característica: Estados Vacíos

  Esquema del escenario: Validación de pantalla "Visitados"
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contrasena "<contrasena>"
    Y hago clic en el botón "Ingresar"
    Cuando selecciono "Visitados"
    Y valido el texto "Aun no visitas a ningun cliente"
    Entonces valido la pantalla de "Visitados"

    Ejemplos:
      | correoElectronico | contrasena |
      | test@test.com     | test123    |
      | Jonathan          | test123    |

  Esquema del escenario: Validación de pantalla "Anulados"
    Dado ingreso el correo electrónico "<correoElectronico>"
    Y ingreso la contrasena "<contrasena>"
    Y hago clic en el botón "Ingresar"
    Cuando selecciono "Anulados"
    Y valido el texto "No has anulado pedidos"
    Y valido el texto "Presiona al cliente para anular un pedido completo"
    Entonces valido la pantalla de "Anulados"

    Ejemplos:
      | correoElectronico | contrasena |
      | test@test.com     | test123    |
      | Jonathan          | test123    |
