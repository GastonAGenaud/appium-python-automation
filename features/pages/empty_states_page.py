from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class EmptyStatesPage(Page):
    anulados_seccion = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Anulados"]')
    visitados_seccion = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="Visitados"]')
    retornados_seccion = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Retornados"]/android.view.ViewGroup')
    entregados_seccion = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Entregados"]/android.view.ViewGroup')
    entregados_sector = (MobileBy.ACCESSIBILITY_ID, "Entregados ")
    no_has_anulado_pedido_txt = [MobileBy.XPATH,
                                 '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/com'
                                 '.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[32]']
    imagen_seccion_anulados = [MobileBy.XPATH,
                               '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/com.horcrux'
                               '.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]']
    no_has_visitado_clientes_txt = [MobileBy.XPATH,
                                    '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/com'
                                    '.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]']
    imagen_seccion_visitados = [MobileBy.XPATH,
                                '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget'
                                '.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                                '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view'
                                '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com'
                                '.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]']
    rebajados_seccion = (MobileBy.ACCESSIBILITY_ID, 'Rebajados')
    pedido_entregado = (MobileBy.XPATH, '//android.widget.TextView[@text="ANTONIO BELLET 345"]')

    def seccion_anulados(self):
        self.click_on_element(self.anulados_seccion)
        self.click_on_element(self.anulados_seccion)
        self.click_on_element(self.anulados_seccion)

    def seccion_retornados(self):
        max_attempts = 4  # Número máximo de intentos
        attempts = 0

        while attempts < max_attempts:
            self.click_on_element(self.retornados_seccion)
            try:
                WebDriverWait(self.driver, 2).until_not(
                    EC.presence_of_element_located(self.retornados_seccion)
                )
                print("El botón ha desaparecido.")
                break
            except TimeoutException:
                print("El botón aún está presente. Intentando nuevamente...")
                attempts += 1
                if attempts == max_attempts:
                    print("Número máximo de intentos alcanzado. El botón aún está presente.")

    def seccion_entregados(self):
        self.click_on_element(self.entregados_seccion)
        self.click_on_element(self.entregados_seccion)

    def seccion_visitados(self):
        self.click_on_element(self.visitados_seccion)

    def sector_entregados(self):
        self.click_on_element(self.entregados_sector)

    def seccion_rebajados(self):
        self.click_on_element(self.rebajados_seccion)

    def valido_txt_seccion_anulados(self):
        self.implicit_wait_visible(self.no_has_anulado_pedido_txt)
        seccion_anulados = self.find_element(self.no_has_anulado_pedido_txt).is_displayed()
        return seccion_anulados

    def valido_imagen_seccion_anulados(self):
        self.implicit_wait_visible(self.imagen_seccion_anulados)
        imagen_anulados = self.find_element(self.imagen_seccion_anulados).is_displayed()
        return imagen_anulados

    def valido_seccion_entregados(self):
        self.implicit_wait_visible(self.pedido_entregado)
        valido_pedido = self.find_element(self.pedido_entregado).is_displayed()
        return valido_pedido

