from typing import List, Union
from sqlalchemy.orm import Session

from . import order_entity, order_schemas


class OrderRepository:
    def get_order(
        db: Session, order_id: int
    ) -> Union[order_schemas.OrderSchema, None]:
        return (
            db.query(order_entity.Order)
            .filter(order_entity.Order.id == order_id)
            .first()
        )

    def get_orders(
        db: Session, skip: int = 0, limit: int = 100
    ) -> List[order_schemas.OrderSchema]:
        return db.query(order_entity.Order).offset(skip).limit(limit).all()

    def create_order(db: Session, order: order_schemas.OrderPayload):
        db_order = order_entity.Order(
            product=order.product,
            amount=order.amount,
            quantity=order.quantity,
            date=order.date,
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
