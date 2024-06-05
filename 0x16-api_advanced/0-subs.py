#!/usr/bin/python3
"""
Module for querying Reddit API for number of subscribers in a subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0

    try:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except ValueError:
        return 0

