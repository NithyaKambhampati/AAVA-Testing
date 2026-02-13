"""
Employee Dashboard: View Personal and Leave Information
Displays employee details, leave balances, and leave history with real-time updates.
"""

from typing import List, Dict
from datetime import datetime

class LeaveType:
    CASUAL = "casual"
    SICK = "sick"
    EARNED = "earned"
    CUSTOM = "custom"

class LeaveRequest:
    def __init__(self, request_id: int, leave_type: str, start_date: str, end_date: str, status: str, reason: str, submitted_at: str, decision_at: str = None, comments: str = None):
        self.request_id = request_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.reason = reason
        self.submitted_at = submitted_at
        self.decision_at = decision_at
        self.comments = comments

class Employee:
    def __init__(self, user_id: str, name: str, email: str, leave_balances: Dict[str, int], leave_history: List[LeaveRequest]):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.leave_balances = leave_balances
        self.leave_history = leave_history

class EmployeeDashboard:
    def __init__(self, employee: Employee):
        self.employee = employee

    def display(self):
        print(f"Employee: {self.employee.name} <{self.employee.email}>")
        print("Leave Balances:")
        for lt, bal in self.employee.leave_balances.items():
            print(f"  {lt.capitalize()}: {bal}")
        print("\nLeave History:")
        for req in self.employee.leave_history:
            print(f"[{req.status}] {req.leave_type.capitalize()} {req.start_date} to {req.end_date} | Reason: {req.reason} | Submitted: {req.submitted_at}")

    def refresh(self, new_balances: Dict[str, int], new_history: List[LeaveRequest]):
        self.employee.leave_balances = new_balances
        self.employee.leave_history = new_history

# Example usage
if __name__ == "__main__":
    leave_history = [
        LeaveRequest(1, LeaveType.CASUAL, "2024-06-01", "2024-06-03", "Approved", "Vacation", "2024-05-20", "2024-05-21", "Enjoy your leave!"),
        LeaveRequest(2, LeaveType.SICK, "2024-06-10", "2024-06-11", "Rejected", "Flu", "2024-06-09", "2024-06-10", "Insufficient balance")
    ]
    emp = Employee("u123", "Alice", "alice@company.com", {LeaveType.CASUAL: 10, LeaveType.SICK: 5}, leave_history)
    dashboard = EmployeeDashboard(emp)
    dashboard.display()
