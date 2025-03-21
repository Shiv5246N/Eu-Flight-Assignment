import requests
import json

# OpenSky API ka URL
url = "https://opensky-network.org/api/states/all"

# API se data fetch karo
response = requests.get(url)

# Response check karo
if response.status_code == 200:
    data = response.json()  # JSON me convert karo
    print(json.dumps(data, indent=4))  # Pretty print JSON
else:
    print(f"Error: {response.status_code}")
