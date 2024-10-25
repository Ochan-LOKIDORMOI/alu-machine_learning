#!/usr/bin/env python3
"""Fetch Home Planets of Sentient Species"""
import requests


def get_sentient_species_homeworlds():
    """Retrieve names of home planets for all sentient species."""
    api_url = "https://swapi-api.hbtn.io/api/species"
    homeworlds = []
    
    response = requests.get(api_url)
    while response.status_code == 200:
        for species in response.json()["results"]:
            homeworld_url = species["homeworld"]
            if homeworld_url:
                homeworld_response = requests.get(homeworld_url)
                homeworlds.append(homeworld_response.json()["name"])
        
        # Fetch next page of species
        next_page = response.json().get("next")
        if next_page:
            response = requests.get(next_page)
        else:
            break
            
    return homeworlds
