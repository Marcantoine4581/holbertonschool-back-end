#!/usr/bin/python3
"""Using a rest API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":

    USER_ID = int(argv[1])

    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    dict_todos = r_todos.json()

    r_users = requests.get("https://jsonplaceholder.typicode.com/users/")
    dict_users = r_users.json()

    for key in dict_users:
        if key.get("id") == USER_ID:
            USERNAME = key.get("username")

    with open("USER_ID.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for key in dict_todos:
            row = []
            if key.get("userId") == USER_ID:
                row.append(USER_ID)
                row.append(USERNAME)
                row.append(key.get("completed"))
                row.append(key.get("title"))
                writer.writerow(row)