import json
from stomp import ConnectionListener

from order_app.api.config.database import Database

from order_app.api.modules.orders.order_repository import OrderRepository
from order_app.api.modules.orders.order_schemas import OrderPayload
from ..config.settings import Settings, get_connection


class OrderListener(ConnectionListener):
    def on_error(self, *args):
        print("Erro na fila")

    def on_message(self, frame):
        print("Salvando pedido...")
        db = next(Database.get_db())
        body = json.loads(frame.body)
        data = OrderPayload(
            amount=body.get("amount"),
            date=body.get("date"),
            product=body.get("product"),
            quantity=body.get("quantity"),
        )
        OrderRepository.create_order(db, data)


class OrderQueue:
    def send_order(payload: str):
        conn = get_connection()
        conn.send(body=payload, destination=Settings().ORDER_QUEUE_DESTINATION)
        conn.disconnect()
