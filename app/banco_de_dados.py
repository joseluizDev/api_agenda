from peewee import SqliteDatabase

# Definir o caminho do banco de dados
db = SqliteDatabase('database.db')


def database_init():
    # Conectar ao banco de dados
    db.connect()

    from app.model.funcionario import Funcionario
    db.create_tables([Funcionario])
    # atualizar o banco de dados
    db.create_tables([Funcionario], safe=True)

    from app.model.cargo import Cargo
    db.create_tables([Cargo])
