from peewee import CharField, Model
from banco_de_dados import db


class Cargo(Model):
    id = CharField(primary_key=True)
    nome = CharField()

    class Meta:
        database = db
        table_name = 'cargos'
