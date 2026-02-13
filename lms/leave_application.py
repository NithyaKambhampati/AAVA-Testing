"""
Employee: Apply for Leave with Validation
Allows employees to submit leave requests with validation for balance, overlap, and date correctness.
"""

from typing import List, Dict
from datetime import datetime
from lms.employee_dashboard import LeaveRequest, Employee, LeaveType

class LeaveValidationError(Exception):
    pass

def validate_leave_request(employee: Employee, leave_type: str, start_date: str, end_date: str, reason: str) -> None:
    # Validate date format
    try:
        sd = datetime.strptime(start_date, "%Y-%m-%d")
        ed = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise LeaveValidationError("Invalid date format. Use YYYY-MM-DD.")
    # End date after or equal to start date
    if ed < sd:
        raise LeaveValidationError("End date cannot be before start date.")
    # Sufficient balance
    days = (ed - sd).days + 1
    if employee.leave_balances.get(leave_type, 0) < days:
        raise LeaveValidationError("Insufficient leave balance.")
    # Overlapping requests
    for req in employee.leave_history:
        if req.status in ["Pending", "Approved"]:
            req_sd = datetime.strptime(req.start_date, "%Y-%m-%d")
            req_ed = datetime.strptime(req.end_date, "%Y-%m-%d")
            if not (ed < req_sd or sd > req_ed):
                raise LeaveValidationError("Leave dates overlap with an existing request.")
    # Leave type exists
    if leave_type not in employee.leave_balances:
        raise LeaveValidationError("Leave type not configured.")

def apply_for_leave(employee: Employee, leave_type: str, start_date: str, end_date: str, reason: str) -> LeaveRequest:
    validate_leave_request(employee, leave_type, start_date, end_date, reason)
    request_id = max([req.request_id for req in employee.leave_history], default=0) + 1
    submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    req = LeaveRequest(request_id, leave_type, start_date, end_date, "Pending", reason, submitted_at)
    employee.leave_history.append(req)
    return req

# Example usage
if __name__ == "__main__":
    from lms.employee_dashboard import Employee, LeaveType
    emp = Employee("u123", "Alice", "alice@company.com", {LeaveType.CASUAL: 10, LeaveType.SICK: 5}, [])
    try:
        req = apply_for_leave(emp, LeaveType.CASUAL, "2024-07-01", "2024-07-03", "Family trip")
        print(f"Leave request submitted: {req.leave_type} {req.start_date} to {req.end_date}, status: {req.status}")
    except LeaveValidationError as e:
        print(f"Error: {e}")
