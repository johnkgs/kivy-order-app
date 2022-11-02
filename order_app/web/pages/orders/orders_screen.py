from typing import List

from kivy.metrics import dp
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

from order_app.web.utils.decorators.debounce import debounce

column_header = [
    ["Produto", dp(128)],
    ["Valor", dp(64)],
    ["Quantidade", dp(64)],
    ["Data", dp(64)],
]

row_data = [["Iphone X", "1000", "3", "20/10/2021"]]


class OrdersScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
                self.data_table.row_data = self.filter(text, row_data)
                return

            self.data_table.row_data = row_data

    def add_processes_data_table_widget(
        self,
    ):
        self.data_table = MDDataTable(
            rows_num=32,
            use_pagination=True,
            pagination_menu_pos="auto",
            column_data=column_header,
            row_data=row_data,
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
