from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from app import api

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/price")
async def get_btc_price(currency_code : Optional[str] = "USD"):
    response = await api.get_btc_price(currency_code=currency_code)
    return response;

@app.post("/new_address")
async def get_new_address():
    response = await api.get_new_address()
    return response;
