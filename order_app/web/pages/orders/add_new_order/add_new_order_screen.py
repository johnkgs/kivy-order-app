from datetime import date

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar


class AddNewOrderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self, *args):
        self.ids.spinner.active = False

        header = MDApp.get_running_app().root.ids.header
        self.toolbar: MDTopAppBar = header.ids.toolbar

        self.change_header()

        today = date.today().strftime("%d/%m/%Y")

        date_field: MDTextField = self.ids.date
        date_field.set_text(self, today)

    def change_header(self):
        self.toolbar.title = "Adicionar novo pedido"
        self.toolbar.left_action_items = [
            [
                "arrow-left",
                lambda x: self.navigation_back(x),
            ]
        ]

    def change_header_back(self, *args):
        self.toolbar.title = "Pedidos"
        self.toolbar.left_action_items = []

    def on_pre_leave(self, *args):
        self.change_header_back()

        if hasattr(self, "error"):
            self.remove_widget(self.error)

    def navigation_back(self, *args):
        self.manager.current = "orders"

    def show_snackbar(self, error: str):
        self.snackbar = Snackbar(text=error)
        self.snackbar.open()

    def on_submit(
        self,
        instance: MDRaisedButton,
        *args,
    ):
        product_field: MDTextField = self.ids.product
        amount_field: MDTextField = self.ids.amount
        quantity_field: MDTextField = self.ids.quantity
        date_field: MDTextField = self.ids.date
        data = {
            "product": product_field,
            "amount": amount_field,
            "quantity": quantity_field,
            "date": date_field,
        }

        has_error = True in [field.error for field in data.values()]

        if has_error:
            errors = list(data.values())
            field_errors = list(filter(lambda x: x.error == True, errors))
            message = ""
            if len(field_errors) > 1:
                fields = list(map(lambda x: x.hint_text, field_errors))
                field_texts = ", ".join(fields)
                message = f"Erro nos campos: {field_texts}"
            if len(field_errors) == 1:
                field_error, *rest = field_errors
                message = f"Erro no campo: {field_error.hint_text}"
            self.show_snackbar(message)
            return

        payload = dict([(key, field.text) for key, field in data.items()])
