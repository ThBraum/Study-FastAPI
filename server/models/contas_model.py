from typing import Optional, List, Dict

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from server.configuration.database import Base
from server.models.usuario_model import UsuarioOutput


class ContasModel(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    tipo = Column(String(50))
    valor = Column(Numeric)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=True)
    usuario = relationship("UsuarioModel", back_populates="contas")


class ContasOutput(BaseModel):
    id: int = Field(None)
    tipo: str = Field(None)
    valor: float = Field(None)
    usuario_id: int = Field(None)

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ContasInput(BaseModel):
    tipo: Optional[str] = None
    valor: Optional[float] = None
    usuario_id: Optional[int] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ContasUsuarioOutput(BaseModel):
    usuario: UsuarioOutput = Field(None)
    contas: List[ContasOutput] = Field(None)

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
