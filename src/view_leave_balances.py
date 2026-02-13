"""
View Leave Balances and History Module

As an employee, I want to view my available leave balances and history of past leave requests so that I can track my leave usage and plan future requests.
"""

from typing import List, Dict

class LeaveRequest:
    def __init__(self, request_id: int, leave_type: str, start_date: str, end_date: str, status: str, comments: str = ""):
        self.request_id = request_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.comments = comments

class Employee:
    def __init__(self, employee_id: int, name: str, leave_balances: Dict[str, int], leave_history: List[LeaveRequest]):
        self.employee_id = employee_id
        self.name = name
        self.leave_balances = leave_balances
        self.leave_history = leave_history

    def get_leave_balances(self) -> Dict[str, int]:
        return self.leave_balances

    def get_leave_history(self) -> List[LeaveRequest]:
        return self.leave_history

if __name__ == "__main__":
    # Example usage
    leave_history = [
        LeaveRequest(1, "Casual", "2024-06-01", "2024-06-02", "Approved"),
        LeaveRequest(2, "Sick", "2024-05-10", "2024-05-11", "Rejected", "Insufficient balance")
    ]
    emp = Employee(1001, "Alice", {"Casual": 10, "Sick": 5, "Earned": 8}, leave_history)
    print("Leave Balances:", emp.get_leave_balances())
    print("Leave History:")
    for lr in emp.get_leave_history():
        print(vars(lr))
