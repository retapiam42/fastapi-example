from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.main import templates

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
