# language: es
@ux
Característica: Validaciones de UX/UI

    @regresion
    Escenario: Valido las zonas de accion de la pantalla de la seccion "Pendientes"
        Dado Ingreso con el conductor a la aplicacion
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Pendientes"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Comenzar ruta"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Modificar"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Más productos"]"
        Y valido la pantalla con la imagen de referencia "//android.view.ViewGroup[@content-desc='Pendientes']" "features/screenshots/referencia_pendientes.png"

    @regresion
    Escenario: Valido las zonas de accion de la pantalla del Pedido
        Dado Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornar todo"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Confirmar"]"
        Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Ver mapa"]"
        Cuando hago click en el boton "Cerrar pedido"
        Entonces valido la pantalla con la imagen de referencia "//android.view.ViewGroup[@content-desc='Retornados']/android.view.ViewGroup" "features/screenshots/referencia_retornado.png"

    @regresion
    Escenario: Valido las zonas de accion de la pantalla del Pedido de la Factura N 404145531
        Dado Ingreso con el conductor a la aplicacion
        Cuando elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145531"
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="+"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="-"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregar"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornar factura"]"
        Y valido el tamaño de zona de accion del boton "(//android.widget.CheckBox[@resource-id="check-product"])[1]/android.view.ViewGroup/android.view.ViewGroup"
        Y valido el tamaño de zona de accion del boton "//com.horcrux.svg.SvgView[@resource-id="closeIcon"]"
        Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@resource-id="formatted-product"]"

    @regresion
    Escenario: Valido las zonas de accion de la pantalla de confirmar entrega de factura N 404145531
        Dado Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "entregar"
        Y selecciono el metodo de pago "Transferencia"
        Y hago click en el boton "Confirmar"
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados "]"

    @regresion
    Escenario: Valido las zonas de accion del desplegable "Ordenar por"
        Dado Reseteo la app
        Y Ingreso con el conductor a la aplicacion
        Cuando hago click en el desplegable
        Entonces valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Más productos"]"
        Y valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Menos productos"]"
        Y valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Ruta"]"

    @regresion
    Escenario: Valido las zonas de accion del modal de modificacion de la ruta
        Dado Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Modificar"
        Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entendido"]"
        Y valido el tamaño de zona de accion del boton "//android.widget.CheckBox/android.view.ViewGroup/android.view.ViewGroup"


    @regresion
    Escenario: Valido las zonas de accion de los botones de modificacion de la ruta
        Dado Reseteo la app
        Y Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Modificar"
        Y hago click en el boton "Entendido"
        Y hago click en el boton "Desplegar"
        Entonces valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Mover hacia arriba"]"
        Y valido el tamaño de zona de accion del boton "//android.view.View[@content-desc="Mover a lo más abajo"]"


    Escenario: Valido las zonas de accion de los botones de la seccion Cuadratura
        Dado Reseteo la app
        Y el usuario ingresa el correo electronico "simple"
        Y el usuario ingresa una contraseña
        Cuando hago click en el boton "Iniciar sesion"
        Y hago click en el boton "Comenzar ruta"
        Y elijo la ruta "Erbi"
        Y selecciono la factura con numero "83908330"
        Y hago click en el boton "entregar"
        Y selecciono el metodo de pago "Transferencia"
        Y hago click en el boton "Confirmar"
        Entonces valido que el metodo de pago fue seleccionado
        Cuando hago click en el boton "Confirmar"
        Y selecciono la factura con numero "8390812"
        Y hago click en el boton "entregar"
        Y selecciono el metodo de pago "Transferencia"
        Y hago click en el boton "Confirmar"
        Entonces valido que el metodo de pago fue seleccionado
        Cuando hago click en el boton "Confirmar"
        Entonces valido que las facturas fueron entregadas
        Cuando hago click en el boton "Confirmar"
        Entonces valido el tamaño de zona de accion del boton "//com.horcrux.svg.SvgView[@resource-id="ChevronRightIcon"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Rebajados"]"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados"]"
        Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@resource-id="chevron-button"])[1]/com.horcrux.svg.SvgView"
        Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@resource-id="chevron-button"])[2]/com.horcrux.svg.SvgView"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Cerrar transporte"]"

    Escenario: Valido las zonas de accion del modal de Metodo de Pago
        Dado Reseteo la app
        Y Ingreso con el conductor a la aplicacion
        Cuando hago click en el boton "Comenzar ruta"
        Y elijo la ruta "El Deseo SPA"
        Y selecciono la factura con numero "404145531"
        Y hago click en el boton "entregar"
        Entonces valido el tamaño de zona de accion del boton "(//android.widget.RadioButton[@resource-id="RadioButtonConfirm"])[1]/android.view.ViewGroup"
        Y valido el tamaño de zona de accion del boton "(//android.widget.RadioButton[@resource-id="RadioButtonConfirm"])[2]/android.view.ViewGroup"
        Y valido el tamaño de zona de accion del boton "(//android.widget.RadioButton[@resource-id="RadioButtonConfirm"])[3]/android.view.ViewGroup"
        Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Confirmar"]"
        Y valido el tamaño de zona de accion del boton "//com.horcrux.svg.SvgView[@resource-id="ChevronRightIcon"]"
