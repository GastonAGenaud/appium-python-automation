# language: es

Característica: UX


    Escenario: Valido las zonas de accion de la pantalla de Inicio de sesion
        Dado estoy en la pantalla de inicio de sesion
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Iniciar sesión"]"

    Escenario: Valido las zonas de accion de la pantalla de la seccion "Pendientes"
        Dado el usuario ingresa el correo electronico "conductor-01"
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
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornar pedido"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Confirmar"]"
        Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Ver mapa"]"

    Escenario: Valido las zonas de accion de la pantalla del Pedido de la Factura N 404145544
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145544"
        Entonces valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Ver mapa"]"
        Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@content-desc="-"])[1]"
        Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@content-desc="+"])[1]"
        Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@content-desc="-"])[2]"
        Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@content-desc="+"])[2]"
        Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@content-desc="-"])[3]"
        Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@content-desc="+"])[3]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregar"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornar pedido"]"
        Y valido el tamaño de zona de accion del boton "(//android.widget.CheckBox[@resource-id="Test Checkbox"])[1]/android.view.ViewGroup/android.view.ViewGroup"
        Y valido el tamaño de zona de accion del boton "(//android.widget.CheckBox[@resource-id="Test Checkbox"])[2]/android.view.ViewGroup/android.view.ViewGroup"
        Y valido el tamaño de zona de accion del boton "(//android.widget.CheckBox[@resource-id="Test Checkbox"])[3]/android.view.ViewGroup/android.view.ViewGroup"
        Y valido el tamaño de zona de accion del boton "//com.horcrux.svg.SvgView[@resource-id="closeIcon"]"

    Escenario: Valido las zonas de accion de la pantalla de confirmar entrega de factura N 404145544
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145544"
        Y hago click en el boton "entregar"
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Rebajados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados "]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Confirmar"]"
        Y valido el tamaño de zona de accion del boton "//com.horcrux.svg.SvgView[@resource-id="closeIcon"]"

    Escenario: Valido las zonas de accion del desplegable "Ordenar por"
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y hago click en el desplegable
        Entonces valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Más productos"]"
        Y valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Menos productos"]"
        Y valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Ruta sugerida"]"

    Escenario: Valido las zonas de accion de los botones de modificacion de la ruta
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Modificar"
        Y hago click en el boton "Entendido"
        Y hago click en el boton "Desplegar"
        Entonces valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Mover hacia arriba"]"
        Y valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Mover a lo más abajo"]"

    Escenario: Valido las zonas de accion del modal de modificacion de la ruta
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y cierro el cuadro de texto
        Y hago click en el boton "Modificar"
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entendido"]"
        Y valido el tamaño de zona de accion del boton "//android.widget.CheckBox[@resource-id="Test Checkbox"]/android.view.ViewGroup/android.view.ViewGroup"

    Escenario: Valido las zonas de accion de la pantalla del Pedidos
        Dado el usuario ingresa el correo electronico "conductor-01"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Entonces valido la pantalla con la imagen de referencia "//android.view.ViewGroup[@content-desc='Retornados']" "features/screenshots/referencia_pedido.png"

    Escenario: Valido las zonas de accion de la pantalla de Inicio de sesion
        Dado estoy en la pantalla de inicio de sesion
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc='Iniciar sesión']"
        Y valido la captura de pantalla del elemento "//android.view.ViewGroup[@content-desc='Iniciar sesión']"
        Y valido la pantalla con la imagen de referencia "//android.view.ViewGroup[@content-desc='Iniciar sesión']" "features/screenshots/referencia_inicio_sesion.png"