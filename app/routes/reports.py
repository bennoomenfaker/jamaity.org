from fastapi import APIRouter, HTTPException
import httpx

reports_router = APIRouter()

REPORTS_API_URL = "https://api.reliefweb.int/v1/reports"

@reports_router.get("/")
async def get_reports(limit: int = 1000, offset: int = 0):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{REPORTS_API_URL}?limit={limit}&offset={offset}")
        response.raise_for_status()
        reports = [
            {"id": report["id"], "title": report["fields"]["title"], "href": report["href"]}
            for report in response.json().get("data", [])
        ]
        return {"count": len(reports), "reports": reports}

@reports_router.get("/{report_id}")
async def get_report(report_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{REPORTS_API_URL}/{report_id}")
        response.raise_for_status()
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            report = data["data"][0]["fields"]
            return {
                "id": report.get("id"),
                "title": report.get("title"),
                "status": report.get("status"),
                "body": report.get("body", "No content available"),
                "url": report.get("url"),
                "source": report.get("source", []),
                "date": report.get("date", {})
            }
        raise HTTPException(status_code=404, detail="Report not found")