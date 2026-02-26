"""
Modify or Cancel Pending Leave Requests
As an employee, I want to modify or cancel my leave request before approval so that I can correct mistakes or change my plans.
"""
from typing import Optional

class LeaveModificationService:
    def __init__(self, leave_request_repo):
        self.leave_request_repo = leave_request_repo

    def modify_request(self, request_id: int, user_id: int, start_date, end_date, reason: Optional[str] = None):
        request = self.leave_request_repo.get(request_id)
        if request.status != 'pending' or request.user_id != user_id:
            return {"success": False, "error": "Cannot modify approved or non-owned request."}
        self.leave_request_repo.update_dates(request_id, start_date, end_date, reason)
        # Restart approval workflow (not implemented)
        return {"success": True}

    def cancel_request(self, request_id: int, user_id: int):
        request = self.leave_request_repo.get(request_id)
        if request.status != 'pending' or request.user_id != user_id:
            return {"success": False, "error": "Cannot cancel approved or non-owned request."}
        self.leave_request_repo.update_status(request_id, 'cancelled')
        return {"success": True}
