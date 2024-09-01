from datetime import datetime

from peewee import AutoField, CharField, DateTimeField, ForeignKeyField, Model

from ..banco_de_dados import db
from .cargo import Cargo


class Funcionario(Model):
    idFuncionario = AutoField()
    email = CharField(unique=True)
    senha = CharField()
    nome = CharField()
    telefone = CharField(max_length=20)
    cpf = CharField(max_length=14, unique=True)
    fotoPerfil = CharField(null=True)
    dataNascimento = DateTimeField(null=True)
    dataCriacao = DateTimeField(default=datetime.now)
    dataUltimaAtualizacao = DateTimeField(default=datetime.now)
    administrador = ForeignKeyField(
        'self', backref='funcionarios_subordinados', on_delete='SET NULL')
    cargo = ForeignKeyField(Cargo, backref='funcionarios')

    def save(self, *args, **kwargs):
        if self.idFuncionario is None:
            self.dataCriacao = datetime.now()
        self.dataUltimaAtualizacao = datetime.now()
        super(Funcionario, self).save(*args, **kwargs)
        if self.administrador is None:
            self.administrador = self
            super(Funcionario, self).save(*args, **kwargs)

    @property
    def is_administrador(self):
        return self.administrador.idFuncionario == self.idFuncionario

    class Meta:
        database = db
        table_name = 'funcionarios'
        
