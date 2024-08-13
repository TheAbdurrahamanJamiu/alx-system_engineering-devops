#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'my-reddit-app'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
        top_ten('python')
        top_ten('nonexistent_subreddit')
