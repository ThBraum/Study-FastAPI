import logging

import uvicorn
from fastapi import FastAPI

from server.controller import usuario_controller, contas_controller

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# Configurações de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

app = FastAPI()

app.include_router(usuario_controller.router)
app.include_router(contas_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8003)
