"""
Modify or Cancel Leave Request Module

As an employee, I want to modify or cancel a pending leave request so that I can correct mistakes or change plans before approval.
"""

from typing import List

class LeaveModificationError(Exception):
    pass

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

    def modify_leave_request(self, request_id, new_start, new_end, new_reason):
        for req in self.leave_history:
            if req.request_id == request_id:
                if req.status != "Pending":
                    raise LeaveModificationError("Only pending requests can be modified.")
                req.start_date = new_start
                req.end_date = new_end
                req.comments = new_reason
                # Simulate manager notification
                print(f"Manager notified: Leave request {request_id} modified.")
                return req
        raise LeaveModificationError("Leave request not found.")

    def cancel_leave_request(self, request_id):
        for i, req in enumerate(self.leave_history):
            if req.request_id == request_id:
                if req.status != "Pending":
                    raise LeaveModificationError("Only pending requests can be cancelled.")
                del self.leave_history[i]
                # Simulate manager notification
                print(f"Manager notified: Leave request {request_id} cancelled.")
                return True
        raise LeaveModificationError("Leave request not found.")

if __name__ == "__main__":
    # Example usage
    leave_history = [LeaveRequest(1, "Casual", "2024-07-01", "2024-07-05", "Pending", "Vacation")]
    emp = Employee(1001, "Alice", {"Casual": 10}, leave_history)
    try:
        emp.modify_leave_request(1, "2024-07-02", "2024-07-06", "Changed plans")
        emp.cancel_leave_request(1)
    except LeaveModificationError as e:
        print(f"Modification/Cancellation failed: {e}")
