#!/usr/bin/python3
"""
Module for querying Reddit API to get all hot posts recursively for a subreddit
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditAPI/0.0.1"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    if response.status_code == 200:
        data = response.json()
        if "data" in data and "children" in data["data"]:
            hot_list.extend(post["data"]["title"] for post in data["data"]["children"])

            if "after" in data["data"]:
                after = data["data"]["after"]
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
