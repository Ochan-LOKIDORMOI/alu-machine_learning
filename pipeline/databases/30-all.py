#!/usr/bin/env python3
"""
lists all documents in a collection
"""


def list_all(mongo_collection):
    """ Return a list of all documents

    Args:
        mongo_collection (mongocollection): Mongo collection

    Returns:
        _type_: _description_
    """
    all_documents = mongo_collection.find()
    documents_list = list(all_documents)

    return documents_list
