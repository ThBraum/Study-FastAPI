import logging
from asyncio.log import logger

from fastapi import HTTPException
from starlette import status

from server.configuration.exceptions import NotFoundException, MissingSessionError
from server.models.usuario_model import UsuarioModel
from server.repository.usuario_repository import UsuarioRepository


class UsuarioService():
    def __init__(self):
        self.repository = UsuarioRepository()
        self.model = UsuarioModel()

    async def get_list_usuarios(self):
        try:
            print("Starting request service...")
            return await self.repository.get_list_usuarios()

        except Exception as e:
            raise MissingSessionError

    async def get_user_by_id(self, id_usuario: int):
            logging.info("Starting request service...")
            if await self.repository.get_user_by_id(id_usuario):
                return await self.repository.get_user_by_id(id_usuario)
            raise NotFoundException

    async def create_user(self, data):
        try:
            logging.info("Starting request service...")
            return await self.repository.create_user(data)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update_user_by_id(self, data, id_usuario: int):
        entity = await self.get_user_by_id(id_usuario)
        if entity is not None:
            return await self.repository.put_entity_by_id(data, id_usuario)


    async def delete_user_by_id(self, id_usuario: int):
        entity = await self.get_user_by_id(id_usuario)
        if entity is not None:
            return await self.repository.delete_user_by_id(id_usuario)
        raise NotFoundException
