from fastapi import FastAPI, Query
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.get("/sunset")
def get_sunset(lat: float,lon: float):
    if not API_KEY:
        return {"error": "API key not configured"}
    city = "London"
    #url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"City '{city}' not found or API error."}
    
    data = response.json()
    sunset_utc = data["sys"]["sunset"]
    sunset_time = datetime.utcfromtimestamp(sunset_utc).strftime("%H:%M:%S UTC")
    
    return {
        "city": city,
        "sunset_time": sunset_time
    }
