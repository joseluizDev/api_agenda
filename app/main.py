from fastapi import FastAPI

from app.banco_de_dados import database_init
from app.routes import autenticacao, funcionarios


def criar_app() -> FastAPI:
    app = FastAPI(title="Minha Aplicação")

    # Inicializar o banco de dados
    database_init()

    # Incluir rotas
    app.include_router(autenticacao.router)
    app.include_router(funcionarios.router)
    return app
