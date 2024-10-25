#!/usr/bin/env python3

"""Script that prints the location of a specific user"""

import requests
import sys
import time

def get_user_location(api_url):
    response = requests.get(api_url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
        current_time = int(time.time())
        minutes_until_reset = (reset_time - current_time) // 60
        print(f"Reset in {minutes_until_reset} min")
    else:
        user_data = response.json()
        location = user_data.get('location')
        if location:
            print(location)
        else:
            print("Location not available")
