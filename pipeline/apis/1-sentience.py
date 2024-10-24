#!/usr/bin/env python3
"""
This module contains the class for the game of Tic Tac Toe.

The module contains the following classes:
"""

import requests

def sentientPlanets():
    base_url = "https://swapi-api.alx-tools.com/species/"
    planets = set()
    next_page = base_url

    while next_page:
        response = requests.get(next_page)
        if response.status_code != 200:
            break

        data = response.json()
        species_list = data['results']
        
        for species in species_list:
            if species.get('designation') == 'sentient':
                homeworld_url = species.get('homeworld')
                if homeworld_url:
                    # Get the homeworld name
                    homeworld_response = requests.get(homeworld_url)
                    if homeworld_response.status_code == 200:
                        homeworld_data = homeworld_response.json()
                        planets.add(homeworld_data.get('name', 'unknown'))
                    else:
                        planets.add('unknown')
                else:
                    planets.add('unknown')
        
        next_page = data.get('next')

    return sorted(planets)
