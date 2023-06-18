from asyncio.log import logger

from fastapi import HTTPException

from server.models.usuario_model import UsuarioModel
from server.repository.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()
        self.model = UsuarioModel()

    async def get_list_usuarios(self):
        try:
            print("Starting request service...")
            lista_usuarios = await self.repository.get_list_usuarios()

            print(f"carregando usuarios {lista_usuarios}")

            return lista_usuarios
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def create_user(self, data):
        try:
            print("Starting request service...")
            usuario = await self.repository.create_or_update(data)

            print(f"carregando usuario {usuario}")

            return usuario
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update_user(self, data, id_usuario: int):
        if id_usuario is None:
            entity = self.model()
        else:
            entity = await self.repository.get_entity_by_id(data, id_usuario)

        return entity

    async def delete_user(self, id_usuario: int):

        entity = await self.repository.delete_user(id_usuario)
        return entity

