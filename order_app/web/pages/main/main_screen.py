from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from order_app.web.utils.path import get_kv_file_path

screen_manager = ScreenManager()


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
