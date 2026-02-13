"""
Leave Application Workflow: Approval, Modification, and Cancellation
Supports approval workflow, modification, and cancellation of leave requests.
"""

from datetime import datetime
from typing import List
from lms.employee_dashboard import LeaveRequest, Employee

class WorkflowError(Exception):
    pass

def cancel_leave_request(employee: Employee, request_id: int) -> None:
    for req in employee.leave_history:
        if req.request_id == request_id:
            if req.status != "Pending":
                raise WorkflowError("Only pending requests can be cancelled.")
            employee.leave_history.remove(req)
            print(f"Leave request {request_id} cancelled.")
            return
    raise WorkflowError("Leave request not found.")

def modify_leave_request(employee: Employee, request_id: int, new_start: str, new_end: str, new_reason: str) -> None:
    for req in employee.leave_history:
        if req.request_id == request_id:
            if req.status != "Pending":
                raise WorkflowError("Only pending requests can be modified.")
            req.start_date = new_start
            req.end_date = new_end
            req.reason = new_reason
            req.submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            req.status = "Pending"
            print(f"Leave request {request_id} modified and resubmitted.")
            return
    raise WorkflowError("Leave request not found.")

def prevent_modification_of_approved(employee: Employee, request_id: int) -> None:
    for req in employee.leave_history:
        if req.request_id == request_id:
            if req.status == "Approved":
                raise WorkflowError("Modification of approved requests is not allowed.")

# Example usage
if __name__ == "__main__":
    from lms.employee_dashboard import LeaveType
    emp = Employee("u123", "Alice", "alice@company.com", {LeaveType.CASUAL: 10}, [])
    # Add a pending request
    req = LeaveRequest(1, LeaveType.CASUAL, "2024-07-10", "2024-07-12", "Pending", "Trip", "2024-06-20 10:00:00")
    emp.leave_history.append(req)
    try:
        modify_leave_request(emp, 1, "2024-07-11", "2024-07-13", "Rescheduled trip")
        cancel_leave_request(emp, 1)
    except WorkflowError as e:
        print(f"Error: {e}")
