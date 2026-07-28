from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#import routes
from .routes.health import router as health_router

app = FastAPI(title="Agentic Document Processor")


#include routes
app.include_router(health_router)

#Allowed origins
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

#CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

