import requests

AUTH_TOKEN = "PUT AUTH TOKEN HERE"

# Blynk HTTP API URL
BLYNK_URL = f"https://blynk.cloud/external/api/update?token={AUTH_TOKEN}"

# Function to send data to Blynk
def send_to_blynk(virtual_pin, value):
    """
    Send data to a virtual pin on the Blynk dashboard.
    
    :param virtual_pin: The virtual pin number (e.g., V0, V1).
    :param value: The value to send (can be int, float, or string).
    """
    url = f"{BLYNK_URL}&{virtual_pin}={value}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Data sent to {virtual_pin}: {value}")
    else:
        print(f"Failed to send data to {virtual_pin}. Status code: {response.status_code}")
        print(response.json())