"""
Apply for Leave Module

As an employee, I want to apply for leave by selecting type, dates, and providing a reason so that my manager can review and approve my absence.
"""

from datetime import datetime
from typing import List, Dict

class LeaveApplicationError(Exception):
    pass

def is_overlapping(new_start, new_end, history):
    for req in history:
        if req.status in ("Pending", "Approved") and not (new_end < req.start_date or new_start > req.end_date):
            return True
    return False

def has_sufficient_balance(leave_type, days, balances):
    return balances.get(leave_type, 0) >= days

def apply_for_leave(employee, leave_type, start_date, end_date, reason):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        if start > end:
            raise LeaveApplicationError("Start date must not be after end date.")
        days = (end - start).days + 1
        if not has_sufficient_balance(leave_type, days, employee.leave_balances):
            raise LeaveApplicationError("Insufficient leave balance.")
        if is_overlapping(start, end, employee.leave_history):
            raise LeaveApplicationError("Overlapping leave request exists.")
        # Simulate leave request submission
        new_request = LeaveRequest(len(employee.leave_history)+1, leave_type, start_date, end_date, "Pending", reason)
        employee.leave_history.append(new_request)
        return new_request
    except Exception as e:
        raise LeaveApplicationError(str(e))

# Reuse LeaveRequest and Employee from view_leave_balances.py or redefine here for standalone
class LeaveRequest:
    def __init__(self, request_id, leave_type, start_date, end_date, status, comments=""):
        self.request_id = request_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.comments = comments

class Employee:
    def __init__(self, employee_id, name, leave_balances, leave_history):
        self.employee_id = employee_id
        self.name = name
        self.leave_balances = leave_balances
        self.leave_history = leave_history

if __name__ == "__main__":
    # Example usage
    emp = Employee(1001, "Alice", {"Casual": 10, "Sick": 5, "Earned": 8}, [])
    try:
        req = apply_for_leave(emp, "Casual", "2024-07-01", "2024-07-05", "Vacation")
        print("Leave Request Submitted:", vars(req))
    except LeaveApplicationError as e:
        print(f"Leave application failed: {e}")
