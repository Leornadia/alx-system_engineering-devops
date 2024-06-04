#!/usr/bin/python3
"""
Module for querying Reddit API to get all hot posts recursively for a subreddit
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])
    
    if not children and not after:
        return None

    for post in children:
        hot_list.append(post.get('data', {}).get('title'))
    
    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    
    return hot_list

