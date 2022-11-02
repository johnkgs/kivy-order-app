import time

from .config.settings import Settings, get_connection
from .queues.order_queue import OrderListener


def start():
    conn = get_connection()
    conn.set_listener("", OrderListener())
    conn.subscribe(
        destination=Settings().ORDER_QUEUE_DESTINATION, id=1, ack="auto"
    )
    while True:
        print("Lendo fila...")
        time.sleep(5)

    conn.disconnect()
