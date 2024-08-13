#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not)."""

import requests
import re
from collections import defaultdict

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = defaultdict(int)
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'my-reddit-app'
    }
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data'].get('after')
            
            # Process titles
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    # Regex to match the exact word, case-insensitive
                    count = len(re.findall(r'\b' + re.escape(word.lower()) + r'\b', title))
                    counts[word.lower()] += count
            
            if after:
                # Recursively fetch the next page
                return count_words(subreddit, word_list, after, counts)
            else:
                # Sort and print results
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            # Invalid subreddit or other error
            return None
    except Exception:
        # Handle any exceptions
        return None
    count_words('python', ['java', 'javascript', 'python'])
