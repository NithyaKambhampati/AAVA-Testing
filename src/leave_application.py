"""
Apply for Leave with Validation
As an employee, I want to apply for various types of leave with start/end dates and reason so that I can request time off in accordance with policy.
"""
from datetime import date
from typing import Optional

class LeaveApplicationService:
    def __init__(self, leave_policy_service, leave_balance_service, leave_request_repo):
        self.leave_policy_service = leave_policy_service
        self.leave_balance_service = leave_balance_service
        self.leave_request_repo = leave_request_repo

    def validate_leave(self, user_id: int, leave_type: str, start: date, end: date) -> Optional[str]:
        if end < start:
            return "End date cannot be before start date."
        if self.leave_request_repo.has_overlapping_request(user_id, start, end):
            return "Overlapping leave request exists."
        balance = self.leave_balance_service.get_balance(user_id, leave_type)
        days_requested = (end - start).days + 1
        if balance < days_requested:
            return "Insufficient leave balance."
        return None

    def apply_leave(self, user_id: int, leave_type: str, start: date, end: date, reason: str = "") -> dict:
        error = self.validate_leave(user_id, leave_type, start, end)
        if error:
            return {"success": False, "error": error}
        leave_request = self.leave_request_repo.create(user_id, leave_type, start, end, reason)
        # Route for approval (not implemented here)
        return {"success": True, "leave_request_id": leave_request.id}
