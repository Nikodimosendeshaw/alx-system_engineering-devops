#!/usr/bin/python3
"""Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        returns a list containing the titles of all hot articles
        for a given subreddit. If no results are found for the
        given subreddit, the function should return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers={"User-Agent": "Daniel"},
                       params={"after": after, 'limit': 100},
                       allow_redirects=False).json()

    if ("data" in res and "children" in res.get("data")):
        for i in res.get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        if "after" in res.get("data") and res.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           res.get("data").get("after"))
        else:
            return hot_list
    return None
