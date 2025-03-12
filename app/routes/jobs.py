from fastapi import APIRouter, HTTPException
import httpx

jobs_router = APIRouter()

JOBS_API_URL = "https://api.reliefweb.int/v1/jobs"

@jobs_router.get("/")
async def get_jobs(limit: int = 1000, offset: int = 0):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JOBS_API_URL}?limit={limit}&offset={offset}")
        response.raise_for_status()
        jobs = response.json().get("data", [])
        return {"count": len(jobs), "jobs": jobs}

@jobs_router.get("/{job_id}")
async def get_job(job_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JOBS_API_URL}/{job_id}")
        response.raise_for_status()
        job = response.json().get("data", [])[0]
        return job