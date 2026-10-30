#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file named USER_ID.csv."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([user_id, username, t.get("completed"),
                             t.get("title")])
