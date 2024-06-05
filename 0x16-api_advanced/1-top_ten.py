#!/usr/bin/python3
"""
Module for querying Reddit API to get the top 10 hot posts for a subreddit
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json().get('data', {}).get('children', [])
        if not results:
            print(None)
            return

        for post in results:
            print(post.get('data', {}).get('title'))
    except ValueError:
        print(None)

