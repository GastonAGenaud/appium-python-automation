# language: es

Característica: Pruebas para la aplicación App Mi Ruta

    Escenario: Inicio de sesión exitoso
        Dado que el usuario ingresa un nombre
        Y el usuario ingresa una contrasena
        Cuando el usuario permite el acceso a la ubicación de este dispositivo
        Entonces estoy en la página principal

    Escenario: Sección Mapa
        Dado que el usuario ingresa un nombre
        Y el usuario ingresa una contrasena
        Cuando el usuario permite el acceso a la ubicación de este dispositivo
        Entonces valido que sea visible el botón Comenzar ruta
        Y valido que sea visible el botón Modificar manualmente

    Esquema del escenario: Sección Lista
        Dado que el usuario ingresa un nombre
        Y el usuario ingresa una contrasena
        Cuando el usuario permite el acceso a la ubicación de este dispositivo
        Y el usuario selecciona la sección Lista
        Entonces valido que sea visible el botón Comenzar ruta
        Y valido que sea visible la "<caracteristica>" con el "<valor>" del pedido

        Ejemplos:
            | caracteristica | valor           |
            |   Local        | Rosa Esveile    |
            |   Direccion    | Padre Tadeo 957 |
            |   Estado       | Abierto         |
            |   Producto     | 32              |
            |   Efectivo     | $460.000        |










