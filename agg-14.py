class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: uses an existing Employee object

    def show_department_info(self):
        print(f"Department: {self.department_name}")
        print("Employee Info:", self.employee.get_details())

# Usage
if __name__ == "__main__":
    # Employee exists independently
    emp = Employee("Ali Khan", 101)

    # Department is given an existing Employee
    dept = Department("IT", emp)

    dept.show_department_info()
