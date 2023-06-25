from decimal import Decimal
from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

from server.configuration.database import Base


#Base é para criar no db
#BaseModel interface do python

class UsuarioModel(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(30))
    numero = Column(Integer)
    salario = Column(Numeric)
    email = Column(String(30))
    senha = Column(String(30))

    contas = relationship("ContasModel", back_populates="usuario")

class UsuarioOutput(BaseModel):
    id: int = Field(None)
    nome: str = Field(None)
    numero: int = Field(None)
    salario: Decimal = Field(None)
    email: str = Field(None)
    senha: str = Field(None)

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UsuarioInput(BaseModel):
    nome: Optional[str] = None
    numero: Optional[int] = None
    salario: Optional[Decimal] = None
    email: Optional[str] = None
    senha: Optional[str] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True