#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'my-reddit-app'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
