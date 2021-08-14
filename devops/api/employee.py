import pandas as pd
import os
from pathlib import Path
from uuid import uuid4

employee_database = os.path.join(Path(__file__).parents[0], 'emplyoee.csv')

# Create an empty database (CSV). if already exists leave it.
if not os.path.exists(employee_database):
    with open(employee_database, 'w') as f:
        f.write('id,first_name,last_name\n')

EMPLOYEES = pd.read_csv(employee_database)


# Add emplyoee info: contain id, first_name, last_name
def create_employee(employee_info: dict):
    global EMPLOYEES
    global employee_database

    # Get existing employees into a dict
    existing_employees = EMPLOYEES.to_dict('records')

    # Create a new UUID as unique ID for the employee
    employee_info['id'] = str(uuid4())

    # Append new emplyoee to the existing
    existing_employees.append(employee_info)

    EMPLOYEES = pd.DataFrame(existing_employees)

    # Write back emplyoee info to CSV
    EMPLOYEES.to_csv(employee_database, index=False)

    return dict(id=employee_info['id'])


# Get emplyee info. 
# TODO: Add error cases.
def get_emplyee_info(employee_id):
    global EMPLOYEES

    record = EMPLOYEES[EMPLOYEES['id'] == employee_id]

    return record.to_dict('records')[0]


# Get all employees
def get_employees(lite=True):
    global EMPLOYEES

    if lite:
        return EMPLOYEES[['id']].to_dict('records')
    else:
        return EMPLOYEES.to_dict('records')
