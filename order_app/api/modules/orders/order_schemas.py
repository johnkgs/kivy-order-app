from datetime import date

from pydantic import BaseModel


class OrderBase(BaseModel):
    product: str
    amount: float
    quantity: int
    date: date


class OrderPayload(OrderBase):
    pass


class OrderSchema(OrderBase):
    id: int

    class Config:
        orm_mode = True
