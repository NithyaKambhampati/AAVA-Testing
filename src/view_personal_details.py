"""
View Personal Details and Leave Information
As an employee, I want to view my personal details, leave balances, and leave history, so that I can make informed decisions about leave applications.
"""

class Employee:
    def __init__(self, emp_id, name, leave_balances, leave_history):
        self.emp_id = emp_id
        self.name = name
        self.leave_balances = leave_balances
        self.leave_history = leave_history

    def view_dashboard(self):
        return {
            'employee_id': self.emp_id,
            'name': self.name,
            'leave_balances': self.leave_balances,
            'leave_history': self.leave_history
        }

# Example usage
if __name__ == '__main__':
    leave_balances = {'casual': 8, 'sick': 5, 'earned': 12}
    leave_history = [
        {'type': 'casual', 'start': '2024-05-01', 'end': '2024-05-02', 'status': 'approved'},
        {'type': 'sick', 'start': '2024-06-10', 'end': '2024-06-11', 'status': 'rejected'}
    ]
    emp = Employee('E123', 'John Doe', leave_balances, leave_history)
    print(emp.view_dashboard())
