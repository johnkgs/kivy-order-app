from datetime import date
import json
from typing import List, Union

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from order_app.queue.queues.order_queue import OrderQueue


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

    def show_snackbar(self, message: str, bg_color="#b23a3a"):
        self.snackbar = Snackbar(text=message, bg_color=bg_color)
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

        payload = dict(
            [(key, self.format_payload(field)) for key, field in data.items()]
        )

        self.ids.spinner.active = True
        self.ids.add.disabled = True

        if isinstance(self.snackbar, Snackbar):
            self.get_root_window().remove_widget(self.snackbar)

        OrderQueue.send_order(json.dumps(payload))
        self.on_success("Pedido enviado com sucesso!")

    def format_payload(self, text_field: MDTextField):
        if text_field.hint_text == "Data":
            data = text_field.text.split("/")
            data.reverse()
            return str("-".join(data))
        return text_field.text

    def on_success(self, message: str):
        self.show_snackbar(message, "#108348")
        self.ids.spinner.active = False
        self.reset_fields()
        self.navigation_back()
        self.ids.add.disabled = False

    def reset_fields(self):
        form_fields: List[
            Union[MDRaisedButton, MDTextField]
        ] = self.ids.form.children

        text_fields = list(
            filter(
                lambda x: not isinstance(x, MDRaisedButton),
                form_fields,
            )
        )

        for text_field in text_fields:
            text_field.text = ""
