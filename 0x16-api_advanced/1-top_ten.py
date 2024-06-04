#!/usr/bin/python3
"""
Module for querying Reddit API for top ten hot posts in a subreddit
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])
    if not data:
        print(None)
        return

    for post in data:
        print(post.get('data', {}).get('title'))

