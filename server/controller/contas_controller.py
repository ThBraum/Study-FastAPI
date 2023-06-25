import logging
from typing import List

from fastapi import APIRouter, Depends

from server.models import Visualization
from server.models.contas_model import ContasOutput, ContasInput
from server.service.contas_service import ContasService

router = APIRouter(prefix='/contas')


@router.get(path="/contas", response_model=List[ContasOutput])
async def listar_contas(
        filter: Visualization = Depends(None),
        commoms: ContasOutput = Depends(None),
):
    logging.info("Starting request to service.listar_usuarios")

    params = dict(commoms)
    params.update(filter)

    service = ContasService()

    return await service.get_list_contas()


@router.post(path="/contas", response_model=ContasInput, status_code=201)
async def post_contas(data: ContasInput):
    logging.info("Starting request to service.post_usuario")

    service = ContasService()
    return await service.create_conta(data)


@router.get(path="/contas/{id_conta}", response_model=ContasOutput, status_code=200)
async def get_conta(id_conta: int):
    logging.info("Starting request to service.get_usuario")

    service = ContasService()
    return await service.get_conta_by_id(id_conta)


@router.put(path="/contas/{id_conta}", response_model=ContasOutput, status_code=200)
async def put_conta(id_conta: int, data: ContasInput):
    logging.info("Starting request to service.put_usuario")

    service = ContasService()
    return await service.update_conta_by_id(data, id_conta)
