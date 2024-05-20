#!/usr/bin/python3
"""
Using a REST API, for a given employee ID, returns information about their
TODO list progress and exports it to a JSON file.
"""
import json
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    """
    Retrieves the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee's name, list of completed tasks,
               and list of all tasks.
    """
    # API endpoint URL
    url = f"{REST_API}/users/{employee_id}/todos"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response data
        todo_list = response.json()

        # Get the employee's name
        employee_name = todo_list[0]["userId"]

        # Get the lists of completed and all tasks
        completed_tasks = [task for task in todo_list if task["completed"]]
        all_tasks = todo_list

        return employee_name, completed_tasks, all_tasks
    else:
        return None, None, None


def export_to_json(employee_id, employee_name, completed_tasks, all_tasks):
    """
    Exports employee's TODO list data to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        completed_tasks (list): List of completed tasks.
        all_tasks (list): List of all tasks.
    """
    # JSON file name
    filename = f"{employee_id}.json"

    # Prepare data in the required format
    data = {
        str(employee_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            } for task in all_tasks
        ]
    }

    # Write data to the JSON file
    with open(filename, mode="w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
        employee_name, completed_tasks, all_tasks = get_employee_todo_progress(employee_id)

        if employee_name is not None:
            export_to_json(employee_id, employee_name, completed_tasks, all_tasks)
        else:
            print("Error: Failed to fetch employee data.")
    else:
        print("Usage: python3 script.py <employee_id>")
