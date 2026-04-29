from fastapi import FastAPI
import requests
from fastapi.responses import JSONResponse, HTMLResponse
from starlette.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory="html")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "test.html")