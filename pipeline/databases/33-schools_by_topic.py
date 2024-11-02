#!/usr/bin/env python3
"""
function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """ returns the lsit of schools having a specific topic

    Args:
        mongo_collection (object): pymongo collection object
        topic (string): topic searched
        
    """
    schools = mongo_collection.find({"topics": topic})
    return schools