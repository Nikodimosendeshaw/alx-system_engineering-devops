#!/usr/bin/python3
"""Get number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
        Return number of subscribers
        If not a valid subreddit, return 0
    """
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'Daniel'})
    if res:
        return res.json()['data']['subscribers']
    return 0
