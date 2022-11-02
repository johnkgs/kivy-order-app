from stomp import Connection
from pydantic import BaseSettings, Field


def get_connection():
    conn = Connection()
    conn.connect(
        Settings().ACTIVEMQ_ADMIN_LOGIN,
        Settings().ACTIVEMQ_ADMIN_PASSWORD,
        wait=True,
    )
    return conn


class Settings(BaseSettings):
    ORDER_QUEUE_DESTINATION: str = Field(
        default="", env="ORDER_QUEUE_DESTINATION"
    )
    ACTIVEMQ_ADMIN_LOGIN: str = Field(default="", env="ACTIVEMQ_ADMIN_LOGIN")
    ACTIVEMQ_ADMIN_PASSWORD: str = Field(
        default="", env="ACTIVEMQ_ADMIN_PASSWORD"
    )
    ACTIVEMQ_USER_LOGIN: str = Field(default="", env="ACTIVEMQ_USER_LOGIN")
    ACTIVEMQ_USER_PASSWORD: str = Field(
        default="", env="ACTIVEMQ_USER_PASSWORD"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
