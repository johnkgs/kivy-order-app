from threading import Thread
from os import system


def start():
    Thread(target=system, args=("poetry run start_api",)).start()
    Thread(target=system, args=("poetry run start_queue",)).start()
    Thread(target=system, args=("poetry run start_web",)).start()
