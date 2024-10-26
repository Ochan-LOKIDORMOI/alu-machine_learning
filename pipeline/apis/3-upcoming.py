#!/usr/bin/env python3
"""How many by rocket?"""
import requests
from datetime import datetime



if __name__ == '__main__':
    """pipeline api"""
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    r = requests.get(url)
    recent = 0


    for dic in r.json():
        new = int(dic["date_unix"])
        if recent == 0 or new < recent:
            recent = new
            launch_name = dic["name"]
            date = dic["date_local"]
            rocket_id = dic["rocket"]


    rurl = "https://api.spacexdata.com/v4/rockets/" + rocket_id
    rocket_data = requests.get(rurl).json()
    rocket_name = rocket_data["name"]


    launchpad_id = dic["launchpad"]
    lurl = "https://api.spacexdata.com/v4/launchpads/" + launchpad_id
    launchpad = requests.get(lurl)
    launchpad_data = launchpad.json()
    launchpad_name = launchpad_data["name"]
    launchpad_local = launchpad_data["locality"]


    string = "{} ({}) {} - {} ({})".format(launch_name, date, rocket_name,
                                            launchpad_name, launchpad_local)


    print(string)
