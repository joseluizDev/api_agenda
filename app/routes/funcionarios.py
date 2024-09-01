from typing import List

from fastapi import APIRouter, HTTPException

from ..esquemas.funcionario import FuncionarioCreate, FuncionarioResponse
from ..model.funcionario import Funcionario

router = APIRouter()


@router.post("/criar-funcionario", response_model=FuncionarioResponse)
def criar_funcionario(funcionario_data: FuncionarioCreate):
    try:
        novo_funcionario = Funcionario.create(**funcionario_data.dict())
        return FuncionarioResponse.model_validate(novo_funcionario)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/funcionarios", response_model=List[FuncionarioResponse])
def listar_funcionarios(idFuncionario: str = None):
    if idFuncionario:
        funcionarios = Funcionario.select().where(
            Funcionario.idFuncionario == idFuncionario)
    else:
        funcionarios = Funcionario.select()
    return [FuncionarioResponse.from_orm(funcionario) for funcionario in funcionarios]


@router.put("/editar-funcionario/{idFuncionario}", response_model=FuncionarioResponse)
def editar_funcionario(idFuncionario: str, funcionario: FuncionarioCreate):
    funcionario_editado = Funcionario.get(
        Funcionario.idFuncionario == idFuncionario)
    funcionario_editado.email = funcionario.email
    funcionario_editado.senha = funcionario.senha
    funcionario_editado.nome = funcionario.nome
    funcionario_editado.telefone = funcionario.telefone
    funcionario_editado.cpf = funcionario.cpf
    funcionario_editado.rg = funcionario.rg
    funcionario_editado.fotoPerfil = funcionario.fotoPerfil
    funcionario_editado.dataNascimento = funcionario.dataNascimento
    funcionario_editado.dataCriacao = funcionario.dataCriacao
    funcionario_editado.dataUltimaAtualizacao = funcionario.dataUltimaAtualizacao
    funcionario_editado.cargo = funcionario.cargo
    funcionario_editado.save()
    return FuncionarioResponse.from_orm(funcionario_editado)
