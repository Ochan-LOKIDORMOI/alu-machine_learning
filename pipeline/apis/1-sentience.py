#!/usr/bin/env python3
"""
This module contains the function to retrieve the home planets
of all sentient species from the SWAPI API.
"""

import requests


def sentientPlanets():
    """
    Fetches and returns a list of names of home planets for all sentient species
    from the SWAPI API.

    The function handles pagination to collect all species marked as 'sentient' and
    retrieves the corresponding homeworld name for each. If a homeworld is not specified
    or if the API call fails, 'unknown' is used as a placeholder.

    Returns:
        list: A sorted list of unique planet names of all sentient species.
    """
    base_url = "https://swapi-api.alx-tools.com/species/"
    planets = set()
    next_page = base_url
    
    while next_page:
        response = requests.get(next_page)
        if response.status_code != 200:
            break
        data = response.json()
        for species in data['results']:
            if species['designation'] == 'sentient':
                homeworld = species['homeworld']
                if homeworld:
                    planet = requests.get(homeworld).json()['name']
                else:
                    planet = 'unknown'
                planets.add(planet)
    next_page = data['next']
    return sorted(list(planets))