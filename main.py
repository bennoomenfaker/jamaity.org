from fastapi import FastAPI
import uvicorn
from app.routes.jobs import jobs_router
from app.routes.reports import reports_router
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()


# Configurer CORS
origins = [
    "http://localhost:3000",
     "*"
    
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jobs_router, prefix="/jobs")
app.include_router(reports_router, prefix="/reports")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Utilise le port de Render ou 8000 par défaut
    uvicorn.run(app, host="0.0.0.0", port=port)
