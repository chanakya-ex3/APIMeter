# test_apimeter.py

import os
import time
import pytest
import requests

BASE_URL = os.getenv("APIMETER_URL", "http://localhost:8080")
ENDPOINT = "/limited"  # Change as per your .env ENDPOINTS

def test_passthrough_allowed():
    resp = requests.get(BASE_URL + ENDPOINT)
    assert resp.status_code == 200

def test_rate_limit_exceeded():
    # Assuming /limited has limit 1 for test
    resp1 = requests.get(BASE_URL + ENDPOINT)
    resp2 = requests.get(BASE_URL + ENDPOINT)
    assert resp2.status_code == 429

def test_default_endpoint():
    resp = requests.get(BASE_URL + "/not-defined")
    # Should return 200 or 429 depending on default rate limit
    assert resp.status_code in (200, 429)

def test_auth_required():
    # Enable auth in your .env for this test
    headers = {"X-App-Id": "demoappid", "X-App-Key": "demokey123"}
    resp = requests.get(BASE_URL + ENDPOINT, headers=headers)
    # Should be 200 if valid, 401 if not
    assert resp.status_code in (200, 401)

def test_auth_missing():
    # Enable auth in your .env for this test
    resp = requests.get(BASE_URL + ENDPOINT)
    assert resp.status_code == 401

@pytest.fixture(scope="module", autouse=True)
def wait_for_server():
    # Wait for the Go server to be up before running tests
    for _ in range(10):
        try:
            requests.get(BASE_URL)
            break
        except Exception:
            time.sleep(1)