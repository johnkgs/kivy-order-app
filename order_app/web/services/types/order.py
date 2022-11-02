from datetime import date
from typing import TypedDict, Literal, Tuple, List, Union


class OrderPayload:
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


class CreateOrderResponse(TypedDict):
    status_code: int
    message: str
    success: bool
    data: Union[Order, OrderResponseError]
