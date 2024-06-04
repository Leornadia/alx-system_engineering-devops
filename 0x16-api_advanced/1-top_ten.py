#!/usr/bin/python3
"""
Module for querying Reddit API for top ten hot posts in a subreddit
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditAPI/0.0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print(None)
        return

    if response.status_code == 200:
        data = response.json()
        if "data" in data and "children" in data["data"]:
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print(None)
    else:
        print(None)
