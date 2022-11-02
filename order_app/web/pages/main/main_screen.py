from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.navigationrail import MDNavigationRail, MDNavigationRailItem

from order_app.web.pages.orders.add_new_order.add_new_order_screen import (
    AddNewOrderScreen,
)
from order_app.web.pages.orders.orders_screen import OrdersScreen
from order_app.web.utils.path import get_kv_file_path

screen_manager = ScreenManager()
screen_manager.add_widget(OrdersScreen(name="orders"))
screen_manager.add_widget(AddNewOrderScreen(name="add_new_order"))


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.title = "Gestão de pedidos"
        return Builder.load_file(get_kv_file_path(__file__, "main_screen.kv"))

    def on_start(self):
        self.initialize_widgets()

    def initialize_widgets(self):
        sm: ScreenManager = self.root.ids.screen_manager
        orders_screen: OrdersScreen = sm.get_screen("orders")
        orders_screen.add_processes_data_table_widget()

    def switch_screen(
        self,
        instance_navigation_rail: MDNavigationRail,
        instance_navigation_rail_item: MDNavigationRailItem,
    ):
        if instance_navigation_rail_item.text == "Pedidos":
            self.root.ids.screen_manager.current = "orders"
