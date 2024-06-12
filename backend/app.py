from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:3000"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)








@app.get("/items/{id}")
async def item(id):
    return {"message":id}
@app.get("/")
async def home():
    return {"message":"Harsh"}