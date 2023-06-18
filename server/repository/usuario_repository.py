from asyncio.log import logger

from sqlalchemy.orm import Session

from server.models.usuario_model import UsuarioModel, UsuarioInput
from server.repository.database_repository import get_db


class UsuarioRepository:
    def __init__(self):
        self._db: Session = next(get_db())

    async def get_list_usuarios(self):
        logger.info("Starting request repository...")
        print("Starting request repository...")

        entity = self._db.query(UsuarioModel).all()

        logger.info(f"carregando usuarios {entity}")
        print(f"carregando usuarios {entity}")

        return entity

    async def create_or_update(self, data):
        entity = UsuarioModel(**data.dict())

        self._db.add(entity)
        self._db.commit()
        self._db.refresh(entity)

        return entity

    async def get_entity_by_id(self, data, id_usuario: int):
        logger.info("Starting request repository...")
        entity = self._db.query(UsuarioModel).filter_by(id=id_usuario).first()
        entity.nome = data.nome
        entity.email = data.email
        entity.senha = data.senha
        entity.numero = data.numero
        entity.salario = data.salario
        self._db.add(entity)
        self._db.commit()
        self._db.refresh(entity)

        return entity

    async def delete_user(self, id_usuario: int):
        logger.info("Starting request repository...")
        entity = self._db.query(UsuarioModel).get(id_usuario) #.delete()
        self._db.delete(entity)
        self._db.commit()

        return entity



