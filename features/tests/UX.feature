# language: es
@ux
Característica: Validaciones de UX/UI


  Escenario: Valido las zonas de accion de la pantalla de la pantalla de inicio de sesion
    Dado estoy en la pantalla de inicio de sesion
    Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Iniciar sesión"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="󰈈"]"


  Escenario: Valido las zonas de accion de la pantalla de la pantalla de vueltas disponibles
    Dado Ingreso con el conductor a la aplicacion
    Entonces valido el tamaño de zona de accion del boton "Vuelta 1, Transporte, 12345678, Zona de carga, 10, Clientes gestionados, 0/9"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Vuelta 1, Transporte, 12345678, Zona de carga, 10, Clientes gestionados, 0/9"]"


  Escenario: Valido las zonas de accion de la pantalla del menu lateral
    Dado Ingreso con el conductor a la aplicacion
    Cuando hago click en el boton "Menu Lateral"
    Entonces valido el tamaño de zona de accion del boton "//android.widget.TextView[@resource-id="title-menu-close-session"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@resource-id="title-menu-terms-conditions"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@resource-id="title-menu-close-session"]"

  Escenario: Valido las zonas de accion de la pantalla de Términos y condiciones
    Dado Ingreso con el conductor a la aplicacion
    Cuando hago click en el boton "Terminos y condiciones"
    Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@resource-id="scrollDownButton"]/com.horcrux.svg.SvgView"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Aceptar términos y condiciones"]"

#  Escenario: Valido las zonas de accion del modal de Eliminar mi cuenta
#    Dado Reseteo la app
#    Y Ingreso con el conductor a la aplicacion
#    Cuando hago click en el boton "Menu Lateral"
#    Y hago click en el boton "Eliminar mi cuenta"
#    Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Sí, eliminar mi cuenta"]"
#    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Cancelar"]"

  @regresion
  Escenario: Valido las zonas de accion de la pantalla de la seccion "Pendientes"
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornados"]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados"]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Pendientes"]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Iniciar vuelta"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Ruta sugerida"]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@resource-id="Home-button-3"]"

  @regresion
  Escenario: Valido las zonas de accion de la pantalla del Pedido
    Dado Ingreso con el conductor a la aplicacion
    Cuando hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornar todo"]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Confirmar"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Ver mapa"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@resource-id="actionCall"]"
    Cuando hago click en el boton "Cerrar pedido"

  @regresion
  Escenario: Valido las zonas de accion de la pantalla del Pedido de la Factura N 404145531
    Dado Ingreso con el conductor a la aplicacion
    Cuando elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "812345672"
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
    Entonces valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Retornados"]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados "]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Confirmar"]"

  @regresion
  Escenario: Valido las zonas de accion del desplegable "Ordenar por"
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el desplegable
    Entonces valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Menos cajas primero"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Menos cajas primero"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Ruta"]"
    Y valido el tamaño de zona de accion del boton "//android.widget.TextView[@text="Personalizado"]"

  Escenario: Valido las zonas de accion de los botones de la seccion Cuadratura
    Dado Reseteo la app
    Y el usuario ingresa el correo electronico "simple"
    Y el usuario ingresa una contraseña
    Cuando hago click en el boton "Iniciar sesion"
    Y selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "LIKE EAT FOODS SPA"
    Y selecciono la factura con numero "812345672"
    Y hago click en el boton "entregar"
    Y hago click en el boton "Confirmar"
    Y selecciono la segunda factura con numero "404145535"
    Y hago click en el boton "entregar"
    Y hago click en el boton "Confirmar"
    Entonces valido que las facturas fueron entregadas
    Cuando hago click en el boton "Confirmar"
    Entonces valido el tamaño de zona de accion del boton "//com.horcrux.svg.SvgView[@resource-id="ChevronRightIcon"]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Rebajados"]"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Entregados"]"
    Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@resource-id="chevron-button"])[1]/com.horcrux.svg.SvgView"
    Y valido el tamaño de zona de accion del boton "(//android.view.ViewGroup[@resource-id="chevron-button"])[2]/com.horcrux.svg.SvgView"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Cerrar vuelta 1"]"

  Escenario: Valido las zonas de accion del modal de Metodo de Pago
    Dado Reseteo la app
    Y Ingreso con el conductor a la aplicacion
    Cuando selecciono la vuelta "Vuelta 1"
    Y hago click en el boton "Iniciar vuelta"
    Y elijo la ruta "El Deseo SPA"
    Y selecciono la factura con numero "812345672"
    Y hago click en la opcion "metodo de pago"
    Entonces valido el tamaño de zona de accion del boton "(//android.widget.RadioButton[@resource-id="RadioButtonConfirm"])[1]/android.view.ViewGroup"
    Y valido el tamaño de zona de accion del boton "(//android.widget.RadioButton[@resource-id="RadioButtonConfirm"])[2]/android.view.ViewGroup"
    Y valido el tamaño de zona de accion del boton "(//android.widget.RadioButton[@resource-id="RadioButtonConfirm"])[3]/android.view.ViewGroup"
    Y valido el tamaño de zona de accion del boton "//android.view.ViewGroup[@content-desc="Confirmar"]"
    Y valido el tamaño de zona de accion del boton "//com.horcrux.svg.SvgView[@resource-id="ChevronRightIcon"]"

