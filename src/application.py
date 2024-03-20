# from features.pages.login_page import LoginPage
from features.pages.main_page import MainPage
# from features.pages.inicio_sesion_page import InicioSesionPage
# from features.pages.modificar_recorrido_page import ModificarRecorridoPage
# from features.pages.rebajar_pedido_page import RebajarPedidoPage
# from features.pages.revisar_pedido_page import RevisarPedidoPage
# from features.pages.anular_pedido_page import AnularPedidoPage
from features.pages.entregar_pedido_page import EntregarPedidoPage
from features.pages.cuadrar_page import CuadrarPage
from features.pages.empty_states_page import EmptyStatesPage


class Application:
    def __init__(self, driver):
        # self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        # self.inicio_sesion_page = InicioSesionPage(driver)
        # self.modificar_recorrido_page = ModificarRecorridoPage(driver)
        # self.rebajar_pedido_page = RebajarPedidoPage(driver)
        # self.revisar_pedido_page = RevisarPedidoPage(driver)
        # self.anular_pedido_page = AnularPedidoPage(driver)
        self.entregar_pedido_page = EntregarPedidoPage(driver)
        self.cuadrar_page = CuadrarPage(driver)
        self.empty_states_page = EmptyStatesPage(driver)


