from fastapi import FastAPI
from .routes.Route import router

app = FastAPI(
    title="Complejidad Algoritimica Backend",
    description="Endpoints to manage the minimum path"
)


app.include_router(router)

app.mount("/", app)
