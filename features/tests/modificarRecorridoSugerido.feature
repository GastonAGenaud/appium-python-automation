Feature: Modificar recorrido sugerido

    Background:
        Given Voy a la pantalla de inicio de sesion

    Scenario Outline: Validacion de la pantalla Comenzar ruta
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        Then valido que se visualice el boton "Comenzar ruta" en la pantalla de rutas

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion de la ruta "<nombreRuta>"
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago clic en el boton "Login"
        And elijo la ruta "<nombreRuta>"
        Then valido la informacion:
            | Texto              |
            | Rosa Esveile       |
            | Padre Tadeo 980    |
            | Abierto            |
            | Cierra a las 13:00 |
            | Productos          |
            | Efectivo           |

        Examples:
            | correoElectronico | contraseña | nombreRuta      |
            | test@test.com     | test123    | Padre Tadeo 957 |
            | Jonathan          | test123    | Entre rios 234  |

    Scenario Outline: Validacion de seleccion de ruta
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        When selecciono la ruta "<nombreRuta>"
        Then se valida que la ruta "<nombreRuta>" este seleccionada

        Examples:
            | correoElectronico | contraseña | nombreRuta      |
            | test@test.com     | test123    | Padre Tadeo 957 |
            | Jonathan          | test123    | Entre rios 234  |

    Scenario Outline: Validacion del boton "Comenzar ruta"
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        When selecciono el boton "Comenzar ruta"
        Then se valida que el boton "Comenzar ruta" haya sido seleccionado correctamente

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion del desplegable "Mas productos"
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        Then valido la informacion:
            | Texto         |
            | Ruta sugerida |
            | Mas lejos     |
            | Mas cerca     |

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion de pantalla de modificar manualmente
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        And selecciono el boton "Modificar manualmente"
        Then valido la informacion del texto de la pantalla de modificacion manual
            | Texto                    |
            | Modifica tu ruta         |
            | Presiona prolongadamente |
            | Entendido                |
            | No volver a mostrar      |

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion de la modificacion de la ruta
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        And selecciono el boton "Modificar manualmente"
        Then selecciono el boton "Entendido"
        And desplazo un cliente hacia una nueva posicion
        And valido el mensaje "Recorrido modificado"

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion de opcion "Pendientes"
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        Then valido la funcionalidad del boton "Pendientes"

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion de opcion "Visitados"
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        Then valido la funcionalidad del boton "Visitados"

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Scenario Outline: Validacion de opcion "Anulados"
        And ingreso el correo electronico "<correoElectronico>"
        And ingreso la contraseña "<contraseña>"
        And hago click en el boton "Ingresar"
        And elijo la ruta "1222654"
        When selecciono el boton "Anulados"
        Then valido la funcionalidad del boton "Anulados"

        Examples:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |
