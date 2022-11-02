import json
from typing import Callable

from kivy.network.urlrequest import UrlRequest

from .types.order import (
    CreateOrderResponse,
    FormatCreateOrderResponse,
    FormatGetOrdersResponse,
    GetOrdersResponse,
    OrderPayload,
)

url = "http://localhost:8000/api/orders"


class OrderService:
    def get_orders(on_success: Callable[[GetOrdersResponse], None]):
        UrlRequest(
            url,
            method="GET",
            on_success=FormatGetOrdersResponse.on_success(on_success),
        )

    def create_order(
        payload: OrderPayload,
        on_success: Callable[[GetOrdersResponse], None],
        on_error: Callable[[GetOrdersResponse], None],
    ) -> CreateOrderResponse:
        UrlRequest(
            url,
            method="POST",
            req_body=json.dumps(payload),
            on_success=FormatCreateOrderResponse.on_success(on_success),
            on_error=FormatCreateOrderResponse.on_error(on_error),
            on_failure=FormatCreateOrderResponse.on_error(on_error),
        )
