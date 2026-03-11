from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app=FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})