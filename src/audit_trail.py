"""
Audit Trail for Leave Actions
As an HR/Admin, I want every leave-related action to be recorded with a timestamp and actor so that compliance and traceability are ensured.
"""

from typing import List, Dict
import datetime

AUDIT_LOGS: List[Dict] = []

def log_leave_action(action: str, actor_id: str, request_id: str, details: str):
    entry = {
        'action': action,
        'actor_id': actor_id,
        'timestamp': datetime.datetime.now(),
        'request_id': request_id,
        'details': details
    }
    AUDIT_LOGS.append(entry)

def get_audit_logs() -> List[Dict]:
    return AUDIT_LOGS

# Example usage
if __name__ == '__main__':
    log_leave_action('create', 'employee1', 'LEAVE123', 'Applied for casual leave')
    log_leave_action('approve', 'manager1', 'LEAVE123', 'Approved leave')
    logs = get_audit_logs()
    for log in logs:
        print(log)
