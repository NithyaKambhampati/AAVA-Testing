"""
Leave Balance Management and Update
Automatically updates leave balances on approval and ensures correctness for rejections/cancellations.
"""

from lms.employee_dashboard import Employee, LeaveRequest
from datetime import datetime

class BalanceUpdateError(Exception):
    pass

def update_leave_balance(employee: Employee, request: LeaveRequest) -> None:
    if request.status == "Approved":
        sd = datetime.strptime(request.start_date, "%Y-%m-%d")
        ed = datetime.strptime(request.end_date, "%Y-%m-%d")
        days = (ed - sd).days + 1
        if employee.leave_balances.get(request.leave_type, 0) < days:
            raise BalanceUpdateError("Insufficient balance for update.")
        employee.leave_balances[request.leave_type] -= days
        print(f"Leave balance updated: {request.leave_type} now {employee.leave_balances[request.leave_type]}")
    elif request.status in ["Rejected", "Cancelled"]:
        # No balance impact
        print(f"No balance update needed for status: {request.status}")
    else:
        raise BalanceUpdateError("Invalid request status for balance update.")

# Example usage
if __name__ == "__main__":
    from lms.employee_dashboard import LeaveType
    emp = Employee("u123", "Alice", "alice@company.com", {LeaveType.CASUAL: 10}, [])
    req = LeaveRequest(1, LeaveType.CASUAL, "2024-07-10", "2024-07-12", "Approved", "Trip", "2024-06-20 10:00:00", "2024-06-21 09:00:00", "Approved")
    update_leave_balance(emp, req)
