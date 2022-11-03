from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from order_app.api.config.database import Database
from order_app.api.utils.tags import RouterTags

from .order_repository import OrderRepository
from .order_schemas import OrderPayload, OrderSchema

router = APIRouter()


@router.get(
    "/orders", tags=[RouterTags.ORDERS], response_model=List[OrderSchema]
)
async def get_orders(
    skip: int = 0, limit: int = 100, db: Session = Depends(Database.get_db)
):
    return OrderRepository.get_orders(db, skip=skip, limit=limit)


@router.post(
    "/orders",
    tags=[RouterTags.ORDERS],
    status_code=HTTPStatus.CREATED,
    response_model=OrderSchema,
)
def create_order(order: OrderPayload, db: Session = Depends(Database.get_db)):
    return OrderRepository.create_order(db, order)
