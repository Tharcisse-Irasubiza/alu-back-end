#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file named USER_ID.json."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    data = {user_id: [{"task": t.get("title"),
                       "completed": t.get("completed"),
                       "username": username} for t in todos]}
    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)
