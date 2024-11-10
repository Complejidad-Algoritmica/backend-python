from fastapi import FastAPI
from .routes.Route import router

#include cors
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Complejidad Algoritmica Backend",
    description="Endpoints to manage the minimum path"
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

app.mount("/", app)
