from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

tickets: list[dict]= [
    {
        "requirement_id": 1,
        "author": "Satwik sanand",
        "description": "change the submit button type from link to button",
        "points": 2
    },
    {
        "requirement_id": 3,
        "author": "Raj",
        "description": "add caching for most frequently visited web pages",
        "points": 4
    }
]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="layout.html", context={"status": "Pending"})

@app.get("/api/v1/tickets")
def get_tickets():
    return tickets