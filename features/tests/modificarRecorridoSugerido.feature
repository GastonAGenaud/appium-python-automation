# language: es

Característica: Modificar recorrido sugerido

    Esquema del escenario: Validacion de la pantalla Comenzar ruta
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Entonces valido que se visualice el boton "Comenzar ruta" en la pantalla de rutas

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion de la ruta "<nombreRuta>"
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago clic en el boton "Login"
        Y elijo la ruta "<nombreRuta>"
        Entonces valido la informacion:
            | Texto              |
            | Rosa Esveile       |
            | Padre Tadeo 980    |
            | Abierto            |
            | Cierra a las 13:00 |
            | Productos          |
            | Efectivo           |

        Ejemplos:
            | correoElectronico | contraseña | nombreRuta      |
            | test@test.com     | test123    | Padre Tadeo 957 |
            | Jonathan          | test123    | Entre rios 234  |

    Esquema del escenario: Validacion de seleccion de ruta
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Y selecciono la ruta "<nombreRuta>"
        Entonces se valida que la ruta "<nombreRuta>" este seleccionada

        Ejemplos:
            | correoElectronico | contraseña | nombreRuta      |
            | test@test.com     | test123    | Padre Tadeo 957 |
            | Jonathan          | test123    | Entre rios 234  |

    Esquema del escenario: Validacion del boton "Comenzar ruta"
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Y selecciono el boton "Comenzar ruta"
        Entonces se valida que el boton "Comenzar ruta" haya sido seleccionado correctamente

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion del desplegable "Mas productos"
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Entonces valido la informacion:
            | Texto         |
            | Ruta sugerida |
            | Mas lejos     |
            | Mas cerca     |

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion de pantalla de modificar manualmente
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Y selecciono el boton "Modificar manualmente"
        Entonces valido la informacion del texto de la pantalla de modificacion manual
            | Texto                    |
            | Modifica tu ruta         |
            | Presiona prolongadamente |
            | Entendido                |
            | No volver a mostrar      |

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion de la modificacion de la ruta
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Y selecciono el boton "Modificar manualmente"
        Y selecciono el boton "Entendido"
        Y desplazo un cliente hacia una nueva posicion
        Entonces valido el mensaje "Recorrido modificado"

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion de opcion "Pendientes"
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Entonces valido la funcionalidad del boton "Pendientes"

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion de opcion "Visitados"
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Entonces valido la funcionalidad del boton "Visitados"

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |

    Esquema del escenario: Validacion de opcion "Anulados"
        Dado ingreso el correo electronico "<correoElectronico>"
        Y ingreso la contraseña "<contraseña>"
        Cuando hago click en el boton "Ingresar"
        Y elijo la ruta "1222654"
        Y selecciono el boton "Anulados"
        Entonces valido la funcionalidad del boton "Anulados"

        Ejemplos:
            | correoElectronico | contraseña |
            | test@test.com     | test123    |
            | Jonathan          | test123    |
