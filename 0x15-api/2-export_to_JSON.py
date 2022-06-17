#!/usr/bin/python3
"""
    script that, using this REST API, for a given employee
    ID, returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get('{}/users/{}'.format(url, sys.argv[1])).json()
    todo_res = requests.get('{}/todos?userId={}'.format(
        url, sys.argv[1])).json()
    innerList = []
    for list_ in todo_res:
        tempDict = {}
        tempDict['task'] = list_.get('title')
        tempDict['completed'] = list_.get('completed')
        tempDict['username'] = user_res.get('username')
        innerList.append(tempDict)
    data = {}
    data[sys.argv[1]] = innerList
    with open('{}.json'.format(sys.argv[1]), 'w') as jsonfile:
        json.dump(data, jsonfile)
