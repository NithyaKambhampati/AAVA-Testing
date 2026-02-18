# leave_modification.py

from datetime import datetime
from typing import List, Dict

class LeaveModification:
    def __init__(self, leave_history: List[Dict]):
        self.leave_history = leave_history
        self.audit_log = []

    def modify_request(self, request_id: int, new_start: str, new_end: str, user_id: str):
        for req in self.leave_history:
            if req['id'] == request_id and req['status'] == 'pending':
                req['start'] = new_start
                req['end'] = new_end
                req['modified_at'] = datetime.utcnow().isoformat()
                req['status'] = 'pending'  # re-enters approval workflow
                self._log_action(user_id, 'modify', req)
                return {"message": "Request modified and re-submitted for approval", "request": req}
        return {"error": "Pending request not found or cannot modify approved/cancelled requests"}

    def cancel_request(self, request_id: int, user_id: str):
        for req in self.leave_history:
            if req['id'] == request_id and req['status'] == 'pending':
                req['status'] = 'cancelled'
                req['cancelled_at'] = datetime.utcnow().isoformat()
                self._log_action(user_id, 'cancel', req)
                return {"message": "Request cancelled", "request": req}
        return {"error": "Pending request not found or cannot cancel approved/cancelled requests"}

    def _log_action(self, user_id: str, action: str, data: Dict):
        self.audit_log.append({
            "user_id": user_id,
            "action": action,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_audit_log(self):
        return self.audit_log

# Example usage
if __name__ == "__main__":
    history = [
        {"id": 1, "type": "casual", "start": "2024-06-10", "end": "2024-06-12", "status": "pending"},
        {"id": 2, "type": "sick", "start": "2024-06-13", "end": "2024-06-14", "status": "approved"}
    ]
    mod = LeaveModification(history)
    print(mod.modify_request(1, '2024-06-11', '2024-06-13', 'emp001'))
    print(mod.cancel_request(1, 'emp001'))
    print(mod.get_audit_log())
