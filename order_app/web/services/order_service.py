import requests
from requests import Response
from .types.order import (
    OrderPayload,
    OrderResponseError,
    CreateOrderResponse,
    GetOrdersResponse,
)

url = "http://localhost:8000/api/orders"


class OrderService:
    def get_orders() -> GetOrdersResponse:
        try:
            response = requests.get(url)
            response.raise_for_status()

            return {
                "status_code": response.status_code,
                "message": "Pedido adicionado com sucesso!",
                "success": True,
                "data": response.json(),
            }
        except requests.exceptions.HTTPError as error:
            response: Response = error.response
            error_response: OrderResponseError = response.json()

            first_error, *rest = error_response.get("detail")
            return {
                "status_code": response.status_code,
                "message": first_error.get("msg"),
                "success": False,
                "data": error_response,
            }

    def create_order(payload: OrderPayload) -> CreateOrderResponse:
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()

            return {
                "status_code": response.status_code,
                "message": "Pedido adicionado com sucesso!",
                "success": True,
                "data": response.json(),
            }
        except requests.exceptions.HTTPError as error:
            response: Response = error.response
            error_response: OrderResponseError = response.json()

            first_error, *rest = error_response.get("detail")
            return {
                "status_code": response.status_code,
                "message": first_error.get("msg"),
                "success": False,
                "data": error_response,
            }
