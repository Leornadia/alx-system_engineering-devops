#!/usr/bin/python3
"""Function to query top ten hot posts on a given subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data", {}).get("children", [])
        for post in results:
            print(post.get("data", {}).get("title"))
        if not results:
            print("None")
    else:
        print("None")
