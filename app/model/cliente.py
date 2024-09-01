from datetime import datetime

from peewee import AutoField, CharField, DateTimeField, ForeignKeyField, Model

from ..banco_de_dados import db
from .funcionario import Funcionario


class Cliente(Model):
    idUsuario = AutoField()
    nome = CharField()
    endereco = CharField()
    cpf = CharField(unique=True)
    Telefone = CharField(unique=True)
    dataNascimento = CharField()
    funcionario = ForeignKeyField(Funcionario, backref='clientes')
