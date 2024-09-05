import requests
import os
from dotenv import load_dotenv

load_dotenv()
BLOCKONOMICS_BASE_API_URL = os.getenv("BLOCKONOMICS_BASE_API_URL")
BLOCKONOMICS_API_KEY = os.getenv("BLOCKONOMICS_API_KEY")

async def get_btc_price(currency_code='USD'):
    url = f"{BLOCKONOMICS_BASE_API_URL}/price?currency={currency_code}"
    headers = {
        "Authorization": f"Bearer {BLOCKONOMICS_API_KEY}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      return response.json()
    else:
      return {"error": "Failed to retrieve data"}

async def get_new_address():
  url = f"{BLOCKONOMICS_BASE_API_URL}/new_address?reset=1"
  headers = {
    "Authorization": f"Bearer {BLOCKONOMICS_API_KEY}"
  }
  response = requests.post(url, json={}, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    return {"error": "Failed to retrieve data"}