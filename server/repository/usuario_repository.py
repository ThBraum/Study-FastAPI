import logging
from asyncio.log import logger

from sqlalchemy.orm import Session

from server.models.contas_model import ContasModel, ContasUsuarioOutput, ContasOutput
from server.models.usuario_model import UsuarioModel, UsuarioInput, UsuarioOutput
from server.repository.database_repository import get_db


class UsuarioRepository:
    def __init__(self):
        self._db: Session = next(get_db())

    async def get_list_usuarios(self):
        logging.info("Starting request repository...")

        entity = self._db.query(UsuarioModel).all()

        return entity

    async def get_user_by_id(self, id_usuario: int):
        logging.info("Starting request repository...")

        return self._db.query(UsuarioModel).filter_by(id=id_usuario).first()

    async def create_user(self, data):
        entity = UsuarioModel(**data.dict())

        self._db.add(entity)
        self._db.commit()
        self._db.refresh(entity)

        return entity

    async def put_entity_by_id(self, data, id_usuario: int):
        logging.info("Starting request repository...")

        entity = await self.get_user_by_id(id_usuario)
        if entity is not None:
            for key, value in data.dict().items():
                setattr(entity, key, value) #entity.key = value

            self._db.merge(entity)
            self._db.commit()
            self._db.refresh(entity)
            return entity

    async def delete_user_by_id(self, id_usuario: int):
        logger.info("Starting request repository...")

        entity = await self.get_user_by_id(id_usuario)
        if entity is None:
            return UsuarioModel()
        else:
            self._db.delete(entity)
            self._db.commit()

        return entity

    async def get_contas_by_usuario(self, id_usuario: int) -> ContasUsuarioOutput:
        logging.info("Starting request repository...")

        user = await self.get_user_by_id(id_usuario)
        contas = self._db.query(ContasModel).filter_by(usuario_id=id_usuario).all()

        return ContasUsuarioOutput(usuario=user, contas=contas)