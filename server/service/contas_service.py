import logging
from fastapi import HTTPException

from server.configuration.exceptions import MissingSessionError, NotFoundException
from server.models.contas_model import ContasModel
from server.repository.contas_repository import ContasRepository
from server.repository.usuario_repository import UsuarioRepository


class ContasService():
    def __init__(self):
        self.repository = ContasRepository()
        self.usuarioRepository = UsuarioRepository()
        self.model = ContasModel()

    async def get_list_contas(self):
        try:
            logging.info("Starting request service...")
            return await self.repository.get_list_accounts()

        except Exception as e:
            raise MissingSessionError

    async def create_conta(self, data):
        try:
            logging.info("Starting request service...")
            return await self.repository.create_accounts(data)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_conta_by_id(self, id_conta: int):
        logging.info("Starting request service...")
        if await self.repository.get_account_by_id(id_conta):
            return await self.repository.get_account_by_id(id_conta)
        raise NotFoundException

    async def update_conta_by_id(self, data, id_conta: int):
        logging.info("Starting request service...")
        if await self.repository.get_account_by_id(id_conta):
            return await self.repository.update_account_by_id(data, id_conta)
        raise NotFoundException
