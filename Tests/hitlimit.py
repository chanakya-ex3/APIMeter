import time
import requests

LIMITED_URL = "http://localhost:8080/limited"
UNLIMITED_URL = "http://localhost:8080/unlimited"
PREMIUM_URL = "http://localhost:8080/premium"

while True:
    try:
        limited_response = requests.get(LIMITED_URL)
        print(f"[LIMITED] Status: {limited_response.status_code}, Response: {limited_response.text}")
    except Exception as e:
        print(f"[LIMITED] Error: {e}")

    try:
        unlimited_response = requests.get(UNLIMITED_URL)
        print(f"[UNLIMITED] Status: {unlimited_response.status_code}, Response: {unlimited_response.text}")
    except Exception as e:
        print(f"[UNLIMITED] Error: {e}")

    try:
        premium_response = requests.get(PREMIUM_URL)
        print(f"[UNLIMITED] Status: {premium_response.status_code}, Response: {premium_response.text}")
    except Exception as e:
        print(f"[UNLIMITED] Error: {e}")

    time.sleep(1)
