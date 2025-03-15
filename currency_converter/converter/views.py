from django.shortcuts import render
from django.http import JsonResponse
import requests
import time

# API Configuration
API_KEY = "0cf21000cf63db4a4dce0dd4"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

# Caching API response to avoid too many calls
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
            return None
    except Exception as e:
        return None

def home(request):
    return render(request, 'index.html')

def api_rates(request):
    rates = get_exchange_rates()
    if rates:
        return JsonResponse({"success": True, "rates": rates})
    else:
        return JsonResponse({"success": False, "error": "Failed to fetch exchange rates"}, status=500)
