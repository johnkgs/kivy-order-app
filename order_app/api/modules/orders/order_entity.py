from sqlalchemy import Column, Date, Float, Integer, String

from order_app.api.config.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String)
    amount = Column(Float)
    quantity = Column(Integer)
    date = Column(Date)
