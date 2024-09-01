from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class FuncionarioBase(BaseModel):
    email: str
    senha: str
    nome: str
    telefone: str
    cpf: str
    fotoPerfil: Optional[str] = None
    dataNascimento: Optional[datetime] = None
    dataCriacao: Optional[datetime] = None
    dataUltimaAtualizacao: Optional[datetime] = None
    administrador_id: Optional[int] = None
    cargo_id: int


class FuncionarioCreate(FuncionarioBase):
    pass


class FuncionarioResponse(FuncionarioBase):
    idFuncionario: int
    email: str
    senha: str
    nome: str
    telefone: str
    cpf: str
    fotoPerfil: Optional[str] = None
    dataNascimento: Optional[datetime] = None
    dataCriacao: Optional[datetime] = None
    dataUltimaAtualizacao: Optional[datetime] = None
    administrador_id: Optional[int] = None
    cargo_id: int

    class Config:
        from_attributes = True
