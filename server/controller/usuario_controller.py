import logging
from typing import List
from fastapi import APIRouter, Depends


from server.models import Visualization
from server.models.usuario_model import UsuarioOutput, UsuarioInput
from server.service.usuario_service import UsuarioService

router = APIRouter(prefix='/usuarios')



@router.get(path="/usuarios", response_model=List[UsuarioOutput])
async def listar_usuarios(
        filter: Visualization = Depends(),
        commoms: UsuarioOutput = Depends(None),
):
    logging.info("Starting request to service.listar_usuarios")

    params = dict(commoms)
    params.update(filter)

    service = UsuarioService()

    return await service.get_list_usuarios()

@router.get(path="/usuarios/{id_usuario}", response_model=UsuarioOutput)
async def get_usuario(id_usuario: int):
    logging.info("Starting request to service.get_usuario")

    service = UsuarioService()
    return await service.get_user_by_id(id_usuario)

@router.post(path="/usuarios", response_model=UsuarioOutput, status_code=201)
async def post_usuario(data: UsuarioInput):
    logging.info("Starting request to service.post_usuario")

    service = UsuarioService()
    return await service.create_user(data)

@router.put(path="/usuarios/{id_usuario}", response_model=UsuarioOutput, status_code=200)
async def put_usuario(id_usuario: int, data: UsuarioInput):
    logging.info("Starting request to service.put_usuario")

    service = UsuarioService()
    return await service.update_user_by_id(data, id_usuario)

@router.delete(path="/usuarios/{id_usuario}", status_code=204)
async def delete_usuario(id_usuario: int):
    logging.info("Starting request to service.delete_usuario")

    service = UsuarioService()
    return await service.delete_user_by_id(id_usuario)