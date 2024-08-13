#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None."""

import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'my-reddit-app'
    }
    params = {'limit': 100}  # Retrieve up to 100 posts per page

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            # Add titles to hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check if there's a next page
            after = data['data'].get('after')
            if after:
                # Recursively fetch the next page
                return recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the final list
                return hot_list
        else:
            # Invalid subreddit or other error
            return None
    except Exception:
        # Handle any exceptions
        return None
    titles = recurse('python')
    print(titles)  # Prints all hot post titles or None if invalid subreddit

