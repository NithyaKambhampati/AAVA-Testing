"""
Leave Application Submission
User Story: As an employee, I want to apply for various leave types by selecting dates and providing reasons so that my leave requests are processed efficiently.
Acceptance Criteria:
- Sufficient balance and valid dates create and route request for approval.
- Insufficient balance or invalid dates: system rejects with error.
"""

from datetime import date
from typing import Dict, Optional, List

class LeaveRequest:
    def __init__(self, employee_id: str, leave_type: str, start_date: date, end_date: date, reason: str):
        self.employee_id = employee_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.status = "pending"

class LeaveApplicationService:
    def __init__(self, balances: Dict[str, Dict[str, int]], requests: List[LeaveRequest]):
        self.balances = balances  # employee_id -> {leave_type: balance}
        self.requests = requests

    def apply_leave(self, employee_id: str, leave_type: str, start_date: date, end_date: date, reason: str) -> str:
        if end_date < start_date:
            return "Error: End date cannot be before start date."
        days = (end_date - start_date).days + 1
        if self.balances[employee_id][leave_type] < days:
            return "Error: Insufficient leave balance."
        # Overlap check
        for req in self.requests:
            if req.employee_id == employee_id and req.status in ["pending", "approved"]:
                if not (end_date < req.start_date or start_date > req.end_date):
                    return "Error: Overlapping leave request."
        leave_req = LeaveRequest(employee_id, leave_type, start_date, end_date, reason)
        self.requests.append(leave_req)
        return "Leave request submitted successfully and routed for approval."

# Example usage:
if __name__ == "__main__":
    balances = {"E123": {"casual": 5, "sick": 8}}
    requests = []
    service = LeaveApplicationService(balances, requests)
    print(service.apply_leave("E123", "casual", date(2024,6,10), date(2024,6,12), "Vacation"))
    print(service.apply_leave("E123", "casual", date(2024,6,11), date(2024,6,13), "Overlap test"))
    print(service.apply_leave("E123", "casual", date(2024,6,15), date(2024,6,14), "Invalid dates"))
    print(service.apply_leave("E123", "casual", date(2024,6,20), date(2024,6,30), "Exceed balance"))
