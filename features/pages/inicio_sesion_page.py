from appium.webdriver.common.mobileby import MobileBy
from features.pages.base_page import Page


class LoginPage(Page):
    CORREO_ELECTRONICO_INPUT_ID = (MobileBy.XPATH, "(//android.widget.EditText[@resource-id='customTextInput'])[1]")
    CONTRASENA_INPUT_ID = (MobileBy.XPATH, "(//android.widget.EditText[@resource-id='customTextInput'])[2]")
    BOTON_INGRESAR_ID = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Ingresar']")
    BOTON_ENTENDIDO_ID = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Entendido']")
    COMENZAR_RUTA_ID = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Comenzar ruta']")
    MENSAJE_ERROR_ID = (MobileBy.ID, "")
    MENSAJE_EXITO_ID = (MobileBy.ID, "")
    BOTON_LOGIN_ID = (MobileBy.ID, "")
    MENSAJE_NO_CONEXION_ID = (MobileBy.ID, "")
    BOTON_RECARGAR_ID = (MobileBy.ID, "")
    MENSAJE_USUARIO_VACIO_ID = (MobileBy.XPATH, "//android.widget.TextView[@text='Tienes que ingresar un correo "
                                                "electrónico']")
    MENSAJE_CARACTERES_ESPECIALES_ID = (MobileBy.XPATH, "//android.widget.TextView[@text='Tienes que ingresar una "
                                                        "contraseña']")
    MENSAJE_CONTRASENA_INCORRECTA_ID = (MobileBy.ID, "")
    BOTON_LOGIN_DESHABILITADO_ID = (MobileBy.ID, "")
    PANTALLA_TRANSPORTE_ID = (MobileBy.ID, "")
    PANTALLA_TRANSPORTE_FINALIZADO_ID = (MobileBy.ID, "")
    PANTALLA_RUTAS_NO_CARGADAS_ID = (MobileBy.ID, "")
    TEXTO_RUTAS_NO_CARGADAS_ID = (MobileBy.ID, "")
    BOTON_ACTUALIZAR_ID = (MobileBy.ID, "")

    def ingresar_correo_electronico(self, correo):
        correo_input = self.find_element(self.CORREO_ELECTRONICO_INPUT_ID)
        correo_input.send_keys(correo)

    def ingresar_contrasena(self, contrasena):
        contrasena_input = self.find_element(self.CONTRASENA_INPUT_ID)
        contrasena_input.send_keys(contrasena)

    def hacer_clic_ingresar(self):
        boton_ingresar = self.find_element(self.BOTON_INGRESAR_ID)
        boton_ingresar.click()

    def validar_mensaje_error_usuario_vacio(self, mensaje):
        mensaje_error = self.find_element(self.MENSAJE_USUARIO_VACIO_ID).text
        assert mensaje_error == mensaje, f"El mensaje de error '{mensaje_error}' no coincide con '{mensaje}'"

    def validar_mensaje_error_caracteres_especiales(self, mensaje):
        mensaje_error_elemento = self.find_element(self.MENSAJE_CARACTERES_ESPECIALES_ID)
        assert mensaje_error_elemento.is_displayed(), "El mensaje de error no se muestra en la página"
        mensaje_error_actual = mensaje_error_elemento.text
        assert mensaje_error_actual == mensaje, f"El mensaje de error '{mensaje_error_actual}' no coincide con '{mensaje}'"

    def validar_mensaje_error_contrasena_incorrecta(self, mensaje):
        mensaje_error_elemento = self.find_element(self.MENSAJE_CONTRASENA_INCORRECTA_ID)
        assert mensaje_error_elemento.is_displayed(), "El mensaje de error no se muestra en la página"
        mensaje_error_actual = mensaje_error_elemento.text
        assert mensaje_error_actual == mensaje, f"El mensaje de error '{mensaje_error_actual}' no coincide con '{mensaje}'"

    def validar_mensaje_exito(self, mensaje):
        mensaje_exito = self.find_element(self.MENSAJE_EXITO_ID).text
        assert mensaje_exito == mensaje, f"El mensaje de éxito '{mensaje_exito}' no coincide con '{mensaje}'"

    def hacer_clic_login(self):
        boton_login = self.find_element(self.BOTON_LOGIN_ID)
        boton_login.click()

    def validar_boton_login_deshabilitado(self):
        boton_login = self.find_element(self.BOTON_LOGIN_DESHABILITADO_ID)
        assert not boton_login.is_enabled(), "El botón de login debería estar deshabilitado"

    def validar_pantalla_transporte(self, mensaje_saludo):
        pantalla_transporte = self.find_element(self.PANTALLA_TRANSPORTE_ID).text
        assert mensaje_saludo in pantalla_transporte, f"El mensaje de saludo '{mensaje_saludo}' no está en la pantalla de transporte"

    def validar_pantalla_transporte_finalizado(self):
        pantalla_transporte_finalizado = self.find_element(self.PANTALLA_TRANSPORTE_FINALIZADO_ID).text
        assert "finalizado" in pantalla_transporte_finalizado, "La pantalla de transporte no está finalizada"

    def validar_pantalla_rutas_no_cargadas(self, mensaje):
        pantalla_rutas_no_cargadas = self.find_element(self.PANTALLA_RUTAS_NO_CARGADAS_ID).text
        assert mensaje in pantalla_rutas_no_cargadas, f"El mensaje '{mensaje}' no está en la pantalla de rutas no cargadas"

    def hacer_clic_actualizar(self):
        boton_actualizar = self.find_element(self.BOTON_ACTUALIZAR_ID)
        boton_actualizar.click()

    def validar_mensaje_no_conexion(self, mensaje):
        mensaje_no_conexion = self.find_element(self.MENSAJE_NO_CONEXION_ID).text
        assert mensaje_no_conexion == mensaje, f"El mensaje de no conexión '{mensaje_no_conexion}' no coincide con '{mensaje}'"

    def hacer_clic_recargar(self):
        boton_recargar = self.find_element(self.BOTON_RECARGAR_ID)
        boton_recargar.click()

    def click_boton_entendido(self):
        boton_entendido = self.find_element(self.BOTON_ENTENDIDO_ID)
        boton_entendido.click()

    def boton_comenzar_ruta(self):
        self.implicit_wait_visible(self.COMENZAR_RUTA_ID)
        boton_comenzar_ruta = self.find_element(self.COMENZAR_RUTA_ID).is_displayed()
        return boton_comenzar_ruta

    def limpiar_campo_usuario(self):
        pass
