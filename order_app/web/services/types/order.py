from datetime import date
from typing import Callable, TypedDict, Literal, Tuple, List, Union
from kivy.network.urlrequest import UrlRequest


class OrderPayload(TypedDict):
    product: str
    amount: float
    quantity: int
    date: date


class Order(OrderPayload):
    id: int


class OrderError(TypedDict):
    loc: Tuple[
        Literal["body"], Literal["product", "amount", "quantity", "date"]
    ]
    msg: str
    type: str


class OrderResponseError(TypedDict):
    detail: List[OrderError]


class BaseResponse(TypedDict):
    status_code: int
    message: str
    success: bool


class CreateOrderResponse(BaseResponse):
    data: Union[Order, OrderResponseError]


class GetOrdersResponse(BaseResponse):
    data: Union[List[Order], OrderResponseError]


class FormatGetOrdersResponse:
    def on_success(
        on_success: Callable[[GetOrdersResponse], None]
    ) -> GetOrdersResponse:
        def success(request: UrlRequest, response_body: List[Order]):
            response: GetOrdersResponse = {
                "status_code": request.resp_status,
                "message": "Pedido listados com sucesso!",
                "success": True,
                "data": response_body,
            }

            on_success(response)

        return success


class FormatCreateOrderResponse:
    def on_success(
        on_success: Callable[[CreateOrderResponse], None]
    ) -> CreateOrderResponse:
        def success(request: UrlRequest, response_body: Order):
            response: CreateOrderResponse = {
                "status_code": request.resp_status,
                "message": "Pedido adicionado com sucesso!",
                "success": True,
                "data": response_body,
            }

            on_success(response)

        return success

    def on_error(
        on_error: Callable[[CreateOrderResponse], None]
    ) -> CreateOrderResponse:
        def error(request: UrlRequest, response_body: OrderResponseError):
            first_error, *rest = response_body.get("detail")
            response: CreateOrderResponse = {
                "status_code": request.resp_status,
                "message": first_error.get("msg"),
                "success": True,
                "data": response_body,
            }

            on_error(response)

        return error
