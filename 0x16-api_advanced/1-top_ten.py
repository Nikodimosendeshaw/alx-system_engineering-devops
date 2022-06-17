#!/usr/bin/python3
"""Get Top Ten hot title"""
import requests


def top_ten(subreddit):
    """
         prints the titles of the first 10 hot posts listed
         not a valid subreddit, print None.
    """
    url = 'https://reddit.com/r/{}/.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'Daniel'})
    if res:
        for i in range(10):
            print(res.json()['data']['children'][i]['data']['title'])
    else:
        print("None")
