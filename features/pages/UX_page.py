from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class UXPage(Page):
    correo_campos = (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="customTextInput"])[1]')

    def valido_tamano_ingresar_btn(self, boton):
        boton = self.driver.find_element(MobileBy.XPATH, f'{boton}')
        tamano = boton.size
        ancho = tamano['width']
        alto = tamano['height']

        if ancho >= 48 and alto >= 48:
            return True
        else:
            return False
