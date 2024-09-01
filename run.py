import uvicorn

from app.main import criar_app

app = criar_app()

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
