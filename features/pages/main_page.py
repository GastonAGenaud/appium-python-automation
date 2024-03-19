from appium.webdriver.common.mobileby import MobileBy
from features.pages.base_page import Page


class MainPage(Page):
    comenzar_ruta_button = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Comenzar ruta"]')
    title_home_page = (MobileBy.XPATH, '//android.widget.TextView[@text="Bienvenido, Test!"]')
    while_using_the_app_button = (MobileBy.XPATH, '//android.widget.Button['
                                                  '@resource-id="com.android.permissioncontroller:id'
                                                  '/permission_allow_foreground_only_button"]')
    modificar_manualmente_button = (MobileBy.XPATH, '//android.widget.TextView[@text="Modificar manualmente"]')
    lista_tab = (MobileBy.XPATH,
                 '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android'
                 '.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view'
                 '.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view'
                 '.ViewGroup[2]/android.view.View/android.view.View['
                 '2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[2]')
    pendientes_btn = (MobileBy.XPATH, '//android.widget')

    def valid_comenzar_ruta_button(self):
        self.implicit_wait_visible(self.comenzar_ruta_button)
        validar_comenzar_ruta = self.find_element(self.comenzar_ruta_button).is_displayed()
        return validar_comenzar_ruta

    def select_while_using_the_app(self):
        self.click_on_element(self.while_using_the_app_button)

    def valid_modificar_manualmente_btn(self):
        self.implicit_wait_visible(self.modificar_manualmente_button)
        valid_modificar_manualmente = self.find_element(self.modificar_manualmente_button).is_displayed()
        return valid_modificar_manualmente

    def select_lista_tab(self):
        self.click_on_element(self.lista_tab)

    def valid_value(self, caracteristica, valor):
        self.implicit_wait_visible(self.comenzar_ruta_button)
        value = self.driver.find_element(MobileBy.XPATH, f'//android.widget.TextView[@resource-id="TestTitle" and '
                                                         f'@text="{valor}"]').is_displayed()
        return value
