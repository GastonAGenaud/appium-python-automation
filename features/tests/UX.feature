# language: es

Característica: UX


    Escenario: Valido las zonas de accion de la pantalla de Inicio de sesion
        Dado estoy en la pantalla de inicio de sesion
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Iniciar sesión"]"

    Escenario: Valido las zonas de accion de la pantalla de la seccion "Pendientes"
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Pendientes"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Comenzar ruta"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Modificar"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Ruta sugerida"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Ruta sugerida"]"

    Escenario: Valido las zonas de accion de la pantalla del Pedido
        Dado el usuario ingresa el correo electronico "user_tests"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Pendientes"]"