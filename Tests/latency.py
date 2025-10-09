import requests
import time

# Define base URLs and endpoints
ports = [3000, 8080]
endpoints = ["/api/slow", "/api/medium", "/api/fast"]

# Store results
results = []

for port in ports:
    print(f"\n--- Testing on port {port} ---")
    for endpoint in endpoints:
        url = f"http://localhost:{port}{endpoint}"
        try:
            start = time.perf_counter()
            response = requests.get(url, timeout=5)
            end = time.perf_counter()
            duration = end - start
            results.append({
                "port": port,
                "endpoint": endpoint,
                "status_code": response.status_code,
                "response_time": round(duration, 4)
            })
            print(f"{endpoint} responded in {duration:.4f} seconds with status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to connect to {url}: {e}")
            results.append({
                "port": port,
                "endpoint": endpoint,
                "status_code": "ERROR",
                "response_time": None
            })

# Optionally display results in a table
print("\n--- Summary ---")
print(f"{'Port':<6} {'Endpoint':<15} {'Status':<8} {'Time (s)':<8}")
for r in results:
    print(f"{r['port']:<6} {r['endpoint']:<15} {r['status_code']:<8} {str(r['response_time']):<8}")

