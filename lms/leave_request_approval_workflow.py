"""
Leave Request Approval Workflow Module
- Manager reviews, approves/rejects leave requests
- Updates leave balances upon approval
- Triggers notifications
"""

from typing import Dict, List

class ApprovalError(Exception):
    pass

class LeaveApprovalService:
    def __init__(self, hr_client, notification_service):
        self.hr_client = hr_client
        self.notification_service = notification_service

    def get_pending_requests(self, manager_id: str) -> List[Dict]:
        return self.hr_client.fetch_pending_requests(manager_id)

    def approve_leave(self, manager_id: str, leave_request_id: str, comment: str = "") -> Dict:
        leave_request = self.hr_client.fetch_leave_request(leave_request_id)
        if leave_request['manager_id'] != manager_id:
            raise ApprovalError("Access denied: Not your team member.")
        self.hr_client.update_leave_status(leave_request_id, 'APPROVED', comment)
        self.hr_client.update_leave_balance(leave_request['employee_id'], leave_request['leave_type'], leave_request['start_date'], leave_request['end_date'])
        self.notification_service.notify_employee(leave_request['employee_id'], f"Your leave request {leave_request_id} has been approved. {comment}")
        return {'status':'APPROVED', 'comment':comment}

    def reject_leave(self, manager_id: str, leave_request_id: str, comment: str = "") -> Dict:
        leave_request = self.hr_client.fetch_leave_request(leave_request_id)
        if leave_request['manager_id'] != manager_id:
            raise ApprovalError("Access denied: Not your team member.")
        self.hr_client.update_leave_status(leave_request_id, 'REJECTED', comment)
        self.notification_service.notify_employee(leave_request['employee_id'], f"Your leave request {leave_request_id} has been rejected. {comment}")
        return {'status':'REJECTED', 'comment':comment}
