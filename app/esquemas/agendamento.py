from datetime import datetime

from pydantic import BaseModel


class AgendamentoBase(BaseModel):
    data_hora: datetime
    descricao: str


class AgendamentoCreate(AgendamentoBase):
    funcionario_id: int
    cliente_id: int


class AgendamentoResponse(AgendamentoBase):
    id: int

    class Config:
        orm_mode = True
