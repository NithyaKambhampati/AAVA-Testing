# approval_workflow.py

from datetime import datetime
from typing import List, Dict

class ApprovalWorkflow:
    def __init__(self, team_leave_requests: List[Dict]):
        self.team_leave_requests = team_leave_requests
        self.audit_log = []

    def review_pending_requests(self):
        return [req for req in self.team_leave_requests if req['status'] == 'pending']

    def approve_request(self, request_id: int, manager_id: str, comments: str = ""):
        for req in self.team_leave_requests:
            if req['id'] == request_id and req['status'] == 'pending':
                req['status'] = 'approved'
                req['manager_comments'] = comments
                req['approved_by'] = manager_id
                req['approved_at'] = datetime.utcnow().isoformat()
                self._log_action(manager_id, 'approve', req)
                return {"message": "Request approved", "request": req}
        return {"error": "Pending request not found"}

    def reject_request(self, request_id: int, manager_id: str, comments: str = ""):
        for req in self.team_leave_requests:
            if req['id'] == request_id and req['status'] == 'pending':
                req['status'] = 'rejected'
                req['manager_comments'] = comments
                req['rejected_by'] = manager_id
                req['rejected_at'] = datetime.utcnow().isoformat()
                self._log_action(manager_id, 'reject', req)
                return {"message": "Request rejected", "request": req}
        return {"error": "Pending request not found"}

    def _log_action(self, manager_id: str, action: str, data: Dict):
        self.audit_log.append({
            "manager_id": manager_id,
            "action": action,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_audit_log(self):
        return self.audit_log

# Example usage
if __name__ == "__main__":
    requests = [
        {"id": 1, "user_id": "emp001", "type": "casual", "start": "2024-06-10", "end": "2024-06-12", "status": "pending"},
        {"id": 2, "user_id": "emp002", "type": "sick", "start": "2024-06-13", "end": "2024-06-14", "status": "pending"}
    ]
    workflow = ApprovalWorkflow(requests)
    print(workflow.review_pending_requests())
    print(workflow.approve_request(1, 'mgr001', 'Approved'))
    print(workflow.reject_request(2, 'mgr001', 'Project deadline'))
    print(workflow.get_audit_log())
