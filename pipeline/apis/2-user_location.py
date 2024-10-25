#!/usr/bin/env python3
import sys
import requests
from datetime import datetime

def fetch_user_location(url):
    try:
        response = requests.get(url)
        
        # Check if the user exists
        if response.status_code == 404:
            print("Not found")
            return
        
        # Handle rate limit
        elif response.status_code == 403:
            reset_timestamp = int(response.headers.get("X-Ratelimit-Reset", 0))
            reset_time = datetime.fromtimestamp(reset_timestamp)
            minutes_remaining = int((reset_time - datetime.now()).total_seconds() / 60)
            print(f"Reset in {minutes_remaining} min")
            return

        # Successful response
        elif response.status_code == 200:
            user_data = response.json()
            location = user_data.get("location", "Location not available")
            print(location)
            return

        # Other status codes
        else:
            print("An error occurred")

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <user_api_url>")
    else:
        user_url = sys.argv[1]
        fetch_user_location(user_url)
