from fastapi import APIRouter
from clients.salvar_formulario import salvar_formulario
from src.schemas.formulario_schema import Formulario
from fastapi.responses import JSONResponse
from loguru import logger
import sys
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db

logger.remove()
logger.add(sys.stderr, level="INFO")
router = APIRouter()

@router.post("/formulario")
def submit_form(formulario: Formulario, db: Session = Depends(get_db)):
    try:
        logger.info('Salvando o formulário no banco de dados:')
        salvar_formulario(db, formulario)
        logger.success('Formulario salvo com sucesso no banco de dados!')
        return JSONResponse(
            status_code=201,
            content={
                "message": "Formulário enviado com sucesso.",
                "data": formulario.model_dump()
            })
    except Exception as erro:
        logger.error(f'Erro ao salvar o formulário: {erro}')
        return JSONResponse(
            status_code=500,
            content={
                "message": "Erro não tratado pela API.",
                "data": str(erro)
            })
