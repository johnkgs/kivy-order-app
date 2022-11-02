import uvicorn
from fastapi import FastAPI

from .config.database import engine
from .modules.orders import order_entity, order_router


order_entity.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(order_router.router, prefix="/api")


def start():
    uvicorn.run(
        "order_app.api.main:app", host="0.0.0.0", port=8000, reload=True
    )
