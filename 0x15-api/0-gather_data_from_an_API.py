#!/usr/bin/python3
"""
Using a REST API, for a given employee ID, returns information about their
TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The employee's TODO list progress.
    """
    # API endpoint URL
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response data
        todo_list = response.json()

        # Count the number of completed tasks
        completed_tasks = sum(task["completed"] for task in todo_list)

        # Get the employee's name
        employee_name = todo_list[0]["userId"]

        # Get the total number of tasks
        total_tasks = len(todo_list)

        # Format the output string
        output = (
            f"Employee {employee_name} is done with "
            f"tasks({completed_tasks}/{total_tasks}):\n"
        )

        # Add the titles of completed tasks
        for task in todo_list:
            if task["completed"]:
                output += f"\t {task['title']}\n"

        return output
    else:
        return f"Error: {response.status_code}"


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
        todo_progress = get_employee_todo_progress(employee_id)
        print(todo_progress)
    else:
        print("Usage: python3 script.py <employee_id>")
