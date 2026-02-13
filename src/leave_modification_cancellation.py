"""
Leave Modification and Cancellation
User Story: As an employee, I want to modify or cancel my leave request before approval, so that I can adjust plans and ensure accurate leave records.
"""

from datetime import datetime
from typing import Optional, Dict

# Simulated requests
LEAVE_REQUESTS = [
    {'request_id': 1, 'email': 'alice@org.com', 'leave_type': 'Sick Leave', 'start_date': '2024-06-10', 'end_date': '2024-06-12', 'status': 'Pending', 'modified_at': None, 'cancelled': False},
    {'request_id': 2, 'email': 'alice@org.com', 'leave_type': 'Casual Leave', 'start_date': '2024-07-01', 'end_date': '2024-07-02', 'status': 'Approved', 'modified_at': None, 'cancelled': False},
]
AUDIT_LOG = []

def modify_leave_request(email: str, request_id: int, new_start: Optional[str] = None, new_end: Optional[str] = None) -> Dict:
    for req in LEAVE_REQUESTS:
        if req['request_id'] == request_id and req['email'] == email:
            if req['status'] != 'Pending' or req['cancelled']:
                return {'success': False, 'error': 'Cannot modify after approval or cancellation.'}
            if new_start:
                req['start_date'] = new_start
            if new_end:
                req['end_date'] = new_end
            req['modified_at'] = datetime.now().isoformat()
            AUDIT_LOG.append({'action': 'Modified', 'request_id': request_id, 'by': email, 'timestamp': req['modified_at']})
            return {'success': True, 'request': req}
    return {'success': False, 'error': 'Request not found.'}

def cancel_leave_request(email: str, request_id: int) -> Dict:
    for req in LEAVE_REQUESTS:
        if req['request_id'] == request_id and req['email'] == email:
            if req['status'] != 'Pending' or req['cancelled']:
                return {'success': False, 'error': 'Cannot cancel after approval or if already cancelled.'}
            req['cancelled'] = True
            req['status'] = 'Cancelled'
            req['modified_at'] = datetime.now().isoformat()
            AUDIT_LOG.append({'action': 'Cancelled', 'request_id': request_id, 'by': email, 'timestamp': req['modified_at']})
            return {'success': True, 'request': req}
    return {'success': False, 'error': 'Request not found.'}

if __name__ == "__main__":
    # Modify a pending request
    print(modify_leave_request('alice@org.com', 1, new_start='2024-06-11'))
    # Cancel a pending request
    print(cancel_leave_request('alice@org.com', 1))
    # Attempt to modify approved request
    print(modify_leave_request('alice@org.com', 2, new_end='2024-07-03'))
    # Attempt to cancel cancelled request
    print(cancel_leave_request('alice@org.com', 1))
