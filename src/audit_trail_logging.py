"""
Audit Trail Logging
User Story: As a compliance officer or admin, I want every leave-related action to be logged with actor and timestamp, so that the system provides traceability and meets compliance requirements.
"""

from typing import List, Dict
from datetime import datetime

AUDIT_LOG: List[Dict] = []


def log_action(action: str, actor: str, details: Dict):
    entry = {
        'action': action,
        'actor': actor,
        'timestamp': datetime.now().isoformat(),
        'details': details
    }
    AUDIT_LOG.append(entry)


def get_audit_log(requesting_user: str, role: str) -> List[Dict]:
    if role == 'HR/Admin' or role == 'Compliance':
        return AUDIT_LOG
    # Employees see only their actions
    return [entry for entry in AUDIT_LOG if entry['actor'] == requesting_user]

if __name__ == "__main__":
    log_action('Create Leave Request', 'alice@org.com', {'request_id': 1})
    log_action('Approve Leave Request', 'bob@org.com', {'request_id': 1})
    log_action('Modify Leave Request', 'alice@org.com', {'request_id': 1})
    print("Audit log for HR/Admin:", get_audit_log('carol@org.com', 'HR/Admin'))
    print("Audit log for Alice:", get_audit_log('alice@org.com', 'Employee'))
