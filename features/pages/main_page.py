from features.credentials import BODY, NAME
from appium.webdriver.common.mobileby import MobileBy
from features.pages.base_page import Page


class MainPage(Page):
    MYWORKDOC_ICON_LIST = (MobileBy.CLASS_NAME, 'android.widget.ImageView')
    title_home_page = (MobileBy.XPATH, '//android.widget.TextView[@text="Bienvenido, Test!"]')
    secondary_title = (MobileBy.XPATH, '//android.widget.TextView[@text="Ruta Digital"]')
    introductory_message = (MobileBy.XPATH, '//android.widget.TextView[@text="Aquí comienza el gran viaje de la nueva '
                                            'app para transportistas"]')
    details_section = (MobileBy.XPATH, '//android.widget.TextView[@text="Details"]')
    pedidos_section = (MobileBy.XPATH, '//android.widget.TextView[@text="Pedidos"]')
    Camera_section = (MobileBy.XPATH, '//android.widget.TextView[@text="Camera"]')
    while_using_the_app_btn = (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]')
    capturar_foto_btn = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Capturar foto"]')
    dont_allow_btn = (MobileBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')
    no_permision_txt = (MobileBy.XPATH, '//android.widget.TextView[@text="No permision"]')
    flatlist_from_Api_title = (MobileBy.XPATH, '//android.widget.TextView[@text="Flatlist from API"]')
    title_text = (MobileBy.XPATH, '//android.widget.TextView[@text="Title"]')
    body_text = (MobileBy.XPATH, '//android.widget.TextView[@text="Body"]')
    agregar_un_post_btn = (MobileBy.XPATH, '//android.widget.Button[@content-desc="Agregar un post"]')
    cambiar_otro_state_btn = (MobileBy.XPATH, '//android.widget.TextView[@text="Cambiar otro state"]')
    quiero_cambiar_mi_nombre_btn = (MobileBy.XPATH, '//android.widget.TextView[@text="Quiero cambiar mi nombre"]')
    argegar_btn = (MobileBy.XPATH, '//android.widget.Button[@content-desc="AGREGAR"]')
    test_title = (MobileBy.XPATH, '//android.widget.TextView[@text="Test"]')
    title_field = (MobileBy.XPATH, '//android.widget.EditText[@text="Title"]')
    body_field = (MobileBy.XPATH, '//android.widget.EditText[@text="Body"]')

    def verify_main_page_is_open(self):
        self.implicit_wait_visible(self.MYWORKDOC_ICON_LIST)
        user_icon_list = self.find_element(self.MYWORKDOC_ICON_LIST).is_displayed()
        return user_icon_list

    def valid_title_home(self):
        self.implicit_wait_visible(self.title_home_page)
        title_home = self.find_element(self.title_home_page).is_displayed()
        return title_home

    def valid_secondary_title_text(self):
        self.implicit_wait_visible(self.secondary_title)
        secondary_title_home = self.find_element(self.secondary_title).is_displayed()
        return secondary_title_home

    def valid_introductory_message(self):
        self.implicit_wait_visible(self.introductory_message)
        introductory_message_home = self.find_element(self.introductory_message).is_displayed()
        return introductory_message_home

    def select_details_section(self):
        self.click_on_element(self.details_section)

    def select_pedidos_section(self):
        self.click_on_element(self.pedidos_section)

    def select_camera_section(self):
        self.click_on_element(self.Camera_section)

    def select_while_using_the_app(self):
        self.click_on_element(self.while_using_the_app_btn)

    def valid_capturar_foto(self):
        self.implicit_wait_visible(self.capturar_foto_btn)
        capturar_foto_button = self.find_element(self.capturar_foto_btn).is_displayed()
        return capturar_foto_button

    def select_dont_allow(self):
        self.click_on_element(self.dont_allow_btn)

    def valid_no_permision_message(self):
        self.implicit_wait_visible(self.no_permision_txt)
        no_permision_message = self.find_element(self.no_permision_txt).is_displayed()
        return no_permision_message

    def valid_flatlist_from_API_title(self):
        self.implicit_wait_visible(self.flatlist_from_Api_title)
        flatlist_from_Api_text = self.find_element(self.flatlist_from_Api_title).is_displayed()
        return flatlist_from_Api_text

    def valid_title_text(self):
        self.implicit_wait_visible(self.title_text)
        title_text = self.find_element(self.title_text).is_displayed()
        return title_text

    def valid_body_text(self):
        self.implicit_wait_visible(self.body_text)
        body_text = self.find_element(self.body_text).is_displayed()
        return body_text

    def valid_agregar_un_post_button(self):
        self.implicit_wait_visible(self.agregar_un_post_btn)
        agregar_un_post_button = self.find_element(self.agregar_un_post_btn).is_displayed()
        return agregar_un_post_button

    def valid_cambiar_otro_state_button(self):
        self.implicit_wait_visible(self.cambiar_otro_state_btn)
        cambiar_otro_state_button = self.find_element(self.cambiar_otro_state_btn).is_displayed()
        return cambiar_otro_state_button

    def valid_quiero_cambiar_mi_nombre_button(self):
        self.implicit_wait_visible(self.quiero_cambiar_mi_nombre_btn)
        quiero_cambiar_mi_nombre_button = self.find_element(self.quiero_cambiar_mi_nombre_btn).is_displayed()
        return quiero_cambiar_mi_nombre_button

    def select_agregar_un_post(self):
        self.click_on_element(self.agregar_un_post_btn)

    def user_input_title(self):
        self.click_on_element(self.title_field)
        self.input(NAME, self.title_field)

    def user_input_body(self):
        self.click_on_element(self.body_field)
        self.input(BODY, self.body_field)

    def select_agregar(self):
        self.click_on_element(self.argegar_btn)

    def valid_the_test_title(self):
        self.implicit_wait_visible(self.test_title)
        test_title = self.find_element(self.test_title).is_displayed()
        return test_title
