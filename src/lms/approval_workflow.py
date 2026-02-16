"""
Approval Workflow for Leave Requests
User Story: As a manager, I want to view, approve, or reject leave requests with comments so that I can manage my team's attendance.
Acceptance Criteria:
- Manager approves/rejects pending requests, employee notified, action logged with comment.
- Alternate approval workflow if manager is on leave.
"""

from typing import List, Dict, Optional

class LeaveRequest:
    def __init__(self, leave_id: str, employee_id: str, status: str = "pending", manager_id: Optional[str] = None, comment: Optional[str] = None):
        self.leave_id = leave_id
        self.employee_id = employee_id
        self.status = status
        self.manager_id = manager_id
        self.comment = comment

class ApprovalService:
    def __init__(self, leave_requests: List[LeaveRequest], manager_status: Dict[str, str]):
        self.leave_requests = leave_requests
        self.manager_status = manager_status  # manager_id -> status ("available"/"on_leave")

    def approve(self, leave_id: str, manager_id: str, comment: str) -> str:
        req = next((r for r in self.leave_requests if r.leave_id == leave_id), None)
        if not req or req.status != "pending":
            return "Error: Leave request not found or not pending."
        if self.manager_status.get(manager_id, "available") == "on_leave":
            return "Alternate approval workflow triggered."
        req.status = "approved"
        req.manager_id = manager_id
        req.comment = comment
        # Notification and audit logging would occur here
        return f"Leave request {leave_id} approved by manager {manager_id}."

    def reject(self, leave_id: str, manager_id: str, comment: str) -> str:
        req = next((r for r in self.leave_requests if r.leave_id == leave_id), None)
        if not req or req.status != "pending":
            return "Error: Leave request not found or not pending."
        if self.manager_status.get(manager_id, "available") == "on_leave":
            return "Alternate approval workflow triggered."
        req.status = "rejected"
        req.manager_id = manager_id
        req.comment = comment
        # Notification and audit logging would occur here
        return f"Leave request {leave_id} rejected by manager {manager_id}."

# Example usage:
if __name__ == "__main__":
    requests = [LeaveRequest("L1", "E123")]
    manager_status = {"M1": "available", "M2": "on_leave"}
    svc = ApprovalService(requests, manager_status)
    print(svc.approve("L1", "M1", "Approved for vacation"))
    print(svc.reject("L1", "M2", "Manager on leave"))
