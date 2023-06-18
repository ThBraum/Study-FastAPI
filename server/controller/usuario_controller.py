from asyncio.log import logger
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server import controller
from server.models import Visualization
from server.models.usuario_model import UsuarioOutput, UsuarioInput
from server.repository.database_repository import get_db
from server.service.usuario_service import UsuarioService

router = APIRouter(prefix='/usuarios')

# Depens = Dependency injection
# commoms = Serve para adionar propriedades em uma rota


# class UsuarioController:
@router.get(path="/usuarios", response_model=List[UsuarioOutput])
async def listar_usuarios(
        filter: Visualization = Depends(),
        commoms: UsuarioOutput = Depends(None),
):
    print("Starting request controller ...")

    params = dict(commoms)
    params.update(filter)

    service = UsuarioService()

    return await service.get_list_usuarios()


@router.post(path="/usuarios", response_model=UsuarioOutput, status_code=201)
async def post_usuario(data: UsuarioInput):
    print("Request controller ...")

    service = UsuarioService()
    return await service.create_user(data)

@router.put(path="/usuarios/{id_usuario}", response_model=UsuarioOutput, status_code=200)
async def put_usuario(id_usuario: int, data: UsuarioInput):
    print("Request controller ...")

    service = UsuarioService()
    return await service.update_user(data, id_usuario)

@router.delete(path="/usuarios/{id_usuario}", status_code=204)
async def delete_usuario(id_usuario: int):
    print("Request controller ...")

    service = UsuarioService()
    return await service.delete_user(id_usuario)