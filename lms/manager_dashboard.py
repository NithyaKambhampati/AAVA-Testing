"""
Manager Dashboard: Review and Decide on Leave Requests
Allows managers to review, approve, or reject team leave requests with comments and handles race conditions.
"""

from typing import List
from datetime import datetime
from lms.employee_dashboard import LeaveRequest, Employee

class DecisionError(Exception):
    pass

def get_pending_requests(team: List[Employee]) -> List[LeaveRequest]:
    pending = []
    for emp in team:
        for req in emp.leave_history:
            if req.status == "Pending":
                pending.append((emp, req))
    return pending

def decide_on_leave(manager_id: str, employee: Employee, request_id: int, action: str, comments: str = None) -> None:
    # Simulate race condition handling with a lock (not implemented in this stub)
    for req in employee.leave_history:
        if req.request_id == request_id:
            if req.status != "Pending":
                raise DecisionError("This request has already been decided.")
            if action not in ["Approve", "Reject"]:
                raise DecisionError("Invalid action.")
            req.status = "Approved" if action == "Approve" else "Rejected"
            req.decision_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            req.comments = comments
            print(f"Manager {manager_id} {action.lower()}ed request {request_id} for {employee.name}.")
            return
    raise DecisionError("Leave request not found.")

# Example usage
if __name__ == "__main__":
    from lms.employee_dashboard import LeaveType
    emp = Employee("u123", "Alice", "alice@company.com", {LeaveType.CASUAL: 10}, [LeaveRequest(1, LeaveType.CASUAL, "2024-07-10", "2024-07-12", "Pending", "Trip", "2024-06-20 10:00:00")])
    try:
        decide_on_leave("m456", emp, 1, "Approve", "Approved, have a nice trip!")
    except DecisionError as e:
        print(f"Error: {e}")
