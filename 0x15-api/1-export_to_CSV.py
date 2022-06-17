#!/usr/bin/python3
"""
    script that, using this REST API, for a given employee
    ID, returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get('{}/users/{}'.format(url, sys.argv[1])).json()
    todo_res = requests.get('{}/todos?userId={}'.format(
        url, sys.argv[1])).json()

    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as csvfile:
        """
            export csv file userId.csv
        """
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for row in todo_res:
            writer.writerow([sys.argv[1], user_res.get('username'),
                            row.get('completed'), row.get('title')])
