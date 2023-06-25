import logging

from sqlalchemy.orm import Session

from server.models.contas_model import ContasModel
from server.repository.database_repository import get_db


class ContasRepository:
    def __init__(self):
        self._db: Session = next(get_db())

    async def get_list_accounts(self):
        logging.info("Starting request repository...")

        entity = self._db.query(ContasModel).all()

        return entity

    async def create_accounts(self, data):
        entity = ContasModel(**data.dict())

        self._db.add(entity)
        self._db.commit()
        self._db.refresh(entity)

        return entity

    async def get_account_by_id(self, id_conta: int):
        logging.info("Starting request repository...")

        return self._db.query(ContasModel).filter_by(id=id_conta).first()

    async def update_account_by_id(self, data, id_conta: int):
        logging.info("Starting request repository...")

        entity = await self.get_account_by_id(id_conta)
        if entity is not None:
            for key, value in data.dict().items():
                setattr(entity, key, value)  # entity.key = value

            self._db.merge(entity)
            self._db.commit()
            self._db.refresh(entity)
            return entity
