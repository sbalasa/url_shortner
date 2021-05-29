#!/usr/bin/env python3
"""
File to shorten the url and serialize/de-serialize the data.
Author: Santhosh Balasa
Email: santhosh.kbr@gmail.com
Date: 28/May/2021
"""

import string
import pickle
import random


# Global
PICKLED_FILE = "cached_urls.pickle"


def deserialize_data():
    """
    Function to de-serialize the data via writing to pickle file.
    Returns:
        data (dict): data from the pickle file
    """
    with open(PICKLED_FILE, "rb") as p:
        data = pickle.load(p)
    return data


def serialize_data(data):
    """
    Function to serialize the data via reading the pickle file.
    Args:
        data (dict): Shortened urls along with its long urls
    """
    with open(PICKLED_FILE, "wb") as p:
        pickle.dump(data, p, protocol=pickle.HIGHEST_PROTOCOL)


def get_cached_urls():
    """
    Function to get all the shortened urls.
    Returns:
        list_of_urls (dict): List of cached urls
    """
    return deserialize_data()


def store_cached_urls(list_of_short_urls, short_url, long_url):
    """
    Function to cache the shortened urls.
    Args:
        list_of_short_urls (dict): List of all shortened urls serialized
        short_url (str): Shortened URL
        long_url (str): Long URL passed by the user
    """
    list_of_short_urls.update({short_url: long_url})
    serialize_data(list_of_short_urls)


def encode(long_url):
    """
    Function to shorten the long url.
    Args:
        long_url (str): Long url passed by the user
    Returns:
        short_url (str): Shortened URL
    """
    list_of_short_urls = get_cached_urls()
    if long_url not in list_of_short_urls.values():
        res = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        list_of_short_urls[res] = long_url
        store_cached_urls(list_of_short_urls, res, long_url)
        return res
    else:
        for k, v in list_of_short_urls.items():
            if v == long_url:
                return k
