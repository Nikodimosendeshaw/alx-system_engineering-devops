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
    user_res = requests.get('{}/users/'.format(url)).json()
    todo_res = requests.get('{}/todos'.format(url)).json()

    usernames, employees = {}, {}
    for user in user_res:
        employees[user.get("id")] = []
        usernames[user.get("id")] = user.get("username")

    for list_ in todo_res:
        tempDict = {}
        tempDict['username'] = usernames.get(list_.get('userId'))
        tempDict['task'] = list_.get('title')
        tempDict['completed'] = list_.get('completed')
        employees.get(list_.get('userId')).append(tempDict)

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(employees, jsonfile)
