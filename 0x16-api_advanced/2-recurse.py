#!/usr/bin/python3
"""Recursive function to query all hot posts on a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        results = data.get("children", [])
        after = data.get("after", None)
        hot_list.extend(post.get("data", {}).get("title") for post in results)

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
