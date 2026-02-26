"""
Leave Approval Workflow for Managers
As a manager, I want to view, approve, or reject leave requests from my team so that I can manage team availability and workload.
"""
from typing import Optional

class LeaveApprovalService:
    def __init__(self, leave_request_repo, notification_service):
        self.leave_request_repo = leave_request_repo
        self.notification_service = notification_service

    def get_pending_requests(self, manager_id: int):
        return self.leave_request_repo.get_team_pending_requests(manager_id)

    def approve_or_reject(self, request_id: int, manager_id: int, approve: bool, comment: Optional[str] = None) -> bool:
        request = self.leave_request_repo.get(request_id)
        if not request or request.manager_id != manager_id:
            return False
        status = 'approved' if approve else 'rejected'
        self.leave_request_repo.update_status(request_id, status, comment)
        self.notification_service.notify_employee(request.user_id, status, comment)
        return True
