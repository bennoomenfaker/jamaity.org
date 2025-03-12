from fastapi import FastAPI
from app.routes.jobs import jobs_router
from app.routes.reports import reports_router

app = FastAPI()

app.include_router(jobs_router, prefix="/jobs")
app.include_router(reports_router, prefix="/reports")