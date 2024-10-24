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
            print(f"Failed to fetch data from {next_page}, status code: {response.status_code}")
            break

        data = response.json()
        species_list = data.get('results', [])

        for species in species_list:
            if species.get('designation') == 'sentient':
                homeworld_url = species.get('homeworld')
                if homeworld_url:
                    # Get the homeworld name
                    homeworld_response = requests.get(homeworld_url)
                    if homeworld_response.status_code == 200:
                        homeworld_data = homeworld_response.json()
                        planet_name = homeworld_data.get('name', 'unknown')
                        if planet_name:
                            planets.add(planet_name)
                        else:
                            print(f"Homeworld name missing for URL: {homeworld_url}")
                    else:
                        print(f"Failed to fetch homeworld data from {homeworld_url}, "
                              f"status code: {homeworld_response.status_code}")
                        planets.add('unknown')
                else:
                    print(f"Homeworld URL missing for species: {species.get('name', 'Unknown Species')}")
                    planets.add('unknown')

        next_page = data.get('next')

    return sorted(planets)
