import uvicorn
from fastapi import FastAPI

import shared
from server.controller import contas_a_pagar_e_receber_controller, usuario_controller
from shared.database import engine, Base

# from server.models import contas
#
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contas_a_pagar_e_receber_controller.router)
app.include_router(usuario_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)