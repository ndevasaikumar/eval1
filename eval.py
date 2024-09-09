employee_directory = {}

def add_employee(emp_id, name, department, salary):
    if emp_id in employee_directory:
        print(f"Employee ID {emp_id} already exists.")
    else:
        employee_directory[emp_id] = {
            'name': name,
            'department': department,
            'salary': salary
        }

def update_employee(emp_id,salary):
            employee_directory[emp_id]['salary'] = salary

def search_employee(emp_id):
    if emp_id not in employee_directory:
        print(f"Employee ID {emp_id} not found.")
    else:
        emp = employee_directory[emp_id]
        print(f"Employee ID: {emp_id}")
        print(f"Name: {emp['name']}")
        print(f"Department: {emp['department']}")
        print(f"Salary: {emp['salary']}")

print(f"Adding Employee Details")
add_employee(1, 'Deva', 'cse', 60000)
add_employee(2, 'sai', 'it', 55000)
add_employee(3, 'Kumar', 'it', 65000)
print(employee_directory)
print(f"Updating Employee details")
update_employee(1, salary=70000)
print(employee_directory)
print(f"Searching Employee Details")
search_employee(1)

