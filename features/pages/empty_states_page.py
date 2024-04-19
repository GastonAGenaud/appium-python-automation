from features.pages.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class EmptyStatesPage(Page):
    anulados_seccion = (MobileBy.XPATH, '(//android.widget.TextView[@text="Anulados"]')
    visitados_seccion = (MobileBy.XPATH, '(//android.view.ViewGroup[@content-desc="Visitados"]')
    no_has_anulado_pedido_txt = [MobileBy.XPATH,
                                 '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[32]']
    imagen_seccion_anulados = [MobileBy.XPATH,
                               '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]']
    no_has_visitado_clientes_txt = [MobileBy.XPATH,
                                    '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[33]']
    imagen_seccion_visitados = [MobileBy.XPATH,
                                '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]']
    rebajados_seccion = (MobileBy.XPATH, '//android.widget.TextView[@text="Rebajados"]')

    def seccion_anulados(self):
        self.click_on_element(self.anulados_seccion)

    def seccion_visitados(self):
        self.click_on_element(self.visitados_seccion)

    def valido_txt_seccion_anulados(self):
        self.implicit_wait_visible(self.no_has_anulado_pedido_txt)
        seccion_anulados = self.find_element(self.no_has_anulado_pedido_txt).is_displayed()
        return seccion_anulados

    def valido_imagen_seccion_anulados(self):
        self.implicit_wait_visible(self.imagen_seccion_anulados)
        imagen_anulados = self.find_element(self.imagen_seccion_anulados).is_displayed()
        return imagen_anulados
