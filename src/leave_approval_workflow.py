"""
Leave Approval Workflow: Manager Review and Action
User Story: As a manager, I want to review and approve or reject leave requests from my team, so that I can manage team availability and ensure proper leave tracking.
"""

from typing import List, Dict, Optional
from datetime import datetime

# Simulated data
TEAM_LEAVE_REQUESTS = [
    {'request_id': 1, 'employee': 'alice@org.com', 'leave_type': 'Sick Leave', 'start_date': '2024-06-10', 'end_date': '2024-06-12', 'reason': 'Medical', 'status': 'Pending', 'comments': [], 'created_at': '2024-06-01T09:00:00'},
]

MANAGER_TEAM = {
    'bob@org.com': ['alice@org.com'],
}

AUDIT_LOG = []

def get_pending_requests(manager_email: str) -> List[Dict]:
    team_members = MANAGER_TEAM.get(manager_email, [])
    return [req for req in TEAM_LEAVE_REQUESTS if req['employee'] in team_members and req['status'] == 'Pending']

def approve_reject_request(manager_email: str, request_id: int, approve: bool, comment: Optional[str] = None) -> Dict:
    for req in TEAM_LEAVE_REQUESTS:
        if req['request_id'] == request_id and req['status'] == 'Pending':
            req['status'] = 'Approved' if approve else 'Rejected'
            if comment:
                req['comments'].append({'by': manager_email, 'comment': comment, 'timestamp': datetime.now().isoformat()})
            log_action = {
                'action': 'Approved' if approve else 'Rejected',
                'request_id': request_id,
                'manager': manager_email,
                'timestamp': datetime.now().isoformat(),
                'comment': comment or ''
            }
            AUDIT_LOG.append(log_action)
            # Simulate employee notification
            print(f"Employee {req['employee']} notified: Your leave request #{request_id} has been {'approved' if approve else 'rejected'}.")
            return {'success': True, 'request': req}
    return {'success': False, 'error': 'Request not found or already processed.'}

if __name__ == "__main__":
    # Manager views pending requests
    pending = get_pending_requests('bob@org.com')
    print(f"Pending requests: {pending}")
    # Manager approves first request
    if pending:
        result = approve_reject_request('bob@org.com', pending[0]['request_id'], True, 'Get well soon!')
        print(result)
    # Manager tries to approve again
    print(approve_reject_request('bob@org.com', 1, True))
