from fastapi import FastAPI

app = FastAPI()

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
def print_hi():
    return {"message": "Hello Satwik!"}

@app.get("/api/v1/tickets")
def get_tickets():
    return tickets