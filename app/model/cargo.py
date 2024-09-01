from peewee import AutoField, CharField, Model

from ..banco_de_dados import db


class Cargo(Model):
    idCargo = AutoField()
    nome = CharField()

    class Meta:
        database = db
        table_name = 'cargos'
