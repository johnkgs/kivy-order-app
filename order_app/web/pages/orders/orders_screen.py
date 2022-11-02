from typing import List

from kivy.metrics import dp
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

from order_app.web.utils.decorators.debounce import debounce
from order_app.web.services.order_service import OrderService
from order_app.web.services.types.order import Order, GetOrdersResponse

column_header = [
    ["Produto", dp(128)],
    ["Valor", dp(64)],
    ["Quantidade", dp(64)],
    ["Data", dp(64)],
]


class OrdersScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.row_data = []
        self.data_table = None

    def on_pre_enter(self, *args):
        if self.ids.get("spinner") is not None:
            self.ids.spinner.active = True

        def on_success(response: GetOrdersResponse):
            data = response.get("data")
            self.row_data = list(map(self.format_data, data))

            if self.data_table is not None:
                self.data_table.row_data = self.row_data

            if self.ids.get("spinner") is not None:
                self.ids.spinner.active = False

        OrderService.get_orders(on_success=on_success)

    def format_data(self, item: Order):
        return [
            str(item.get("product")),
            str(item.get("amount")),
            str(item.get("quantity")),
            str(self.format_date(item.get("date"))),
        ]

    def format_date(self, date: str):
        data = date.split("-")
        data.reverse()
        return "/".join(data)

    def filter(
        self,
        text: str,
        data: List[List[str]],
    ):
        new_data: List[List[str]] = []
        for item in data:
            line = " ".join(item)
            if text.lower() in line.lower():
                new_data.append(item)
        return new_data

    @debounce(0.1)
    def set_orders_list(self, text="", search=False):
        if search:
            if len(text) > 0:
                self.data_table.row_data = self.filter(text, self.row_data)
                return

            self.data_table.row_data = self.row_data

    def add_processes_data_table_widget(
        self,
    ):
        self.data_table = MDDataTable(
            rows_num=32,
            use_pagination=True,
            pagination_menu_pos="auto",
            column_data=column_header,
            row_data=self.row_data,
        )

        pagination_label: MDLabel = self.data_table.pagination.children[-1]
        pagination_label.text = "Linhas por página"

        self.ids.recycle_view.add_widget(self.data_table)

    def on_press_add_new_order(
        self,
        instance: MDRectangleFlatIconButton,
        *args,
    ):
        self.manager.current = "add_new_order"
