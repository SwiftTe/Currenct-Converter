import requests
import time

API_KEY = "your_api_key_here"  
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

cached_rates = None
last_updated = 0
CACHE_TIME = 300  # Cache for 5 minutes

def get_exchange_rates():
    global cached_rates, last_updated
    if cached_rates and (time.time() - last_updated < CACHE_TIME):
        return cached_rates  # Return cached data
    
    try:
        response = requests.get(BASE_URL)
        data = response.json()
        if response.status_code == 200:
            cached_rates = data["conversion_rates"]
            last_updated = time.time()
            return cached_rates
        else:
            print("Error fetching data:", data["error-type"])
            return None
    except Exception as e:
        print("Failed to fetch exchange rates:", str(e))
        return None
