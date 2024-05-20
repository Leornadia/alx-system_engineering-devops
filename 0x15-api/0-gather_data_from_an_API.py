#!/usr/bin/python3

import requests

def get_todo_progress(api_url, employee_id):
  """
  Fetches and displays an employee's TODO list progress from a REST API.

  Args:
      api_url (str): The base URL of the REST API.
      employee_id (int): The ID of the employee whose progress to retrieve.
  """
  endpoint = f"{api_url}/users/{employee_id}/todos"

  try:
    response = requests.get(endpoint)
    response.raise_for_status()  # Raise exception for non-200 status codes
    data = response.json()

    completed_tasks = sum(task["completed"] for task in data)
    total_tasks = len(data)

    print(f"Employee {data[0]['name']} is done with tasks({completed_tasks}/{total_tasks}):")

    for task in data:
      if task["completed"]:
        print(f"\t{task['title']}")

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data for employee ID {employee_id}: {e}")

if __name__ == "__main__":
  # Replace with the actual REST API URL for employee data
  api_url = "https://your_api_endpoint.com"

  # Get employee ID from command line argument (assuming a single argument)
  try:
    employee_id = int(input("Enter employee ID: "))
    get_todo_progress(api_url, employee_id)
  except ValueError:
    print("Invalid employee ID. Please enter an integer.")


