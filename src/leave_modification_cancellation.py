"""
Leave Modification/Cancellation Module
- Allows employees to modify or cancel leave requests before approval
- Prevents modification/cancellation after approval
"""

from typing import List, Dict

LEAVE_REQUESTS = [
    {'id': 1, 'employee': 'alice@company.com', 'type': 'CASUAL', 'start': '2024-06-10', 'end': '2024-06-12', 'status': 'PENDING'},
    {'id': 2, 'employee': 'alice@company.com', 'type': 'SICK', 'start': '2024-06-15', 'end': '2024-06-16', 'status': 'APPROVED'},
]


def modify_leave(request_id: int, employee_email: str, new_start: str, new_end: str) -> Dict:
    for req in LEAVE_REQUESTS:
        if req['id'] == request_id and req['employee'] == employee_email:
            if req['status'] == 'PENDING':
                req['start'] = new_start
                req['end'] = new_end
                req['status'] = 'PENDING'  # Workflow restarts
                return {'status': 'MODIFIED', 'request': req}
            else:
                return {'error': 'Cannot modify approved/rejected request.'}
    return {'error': 'Request not found.'}

def cancel_leave(request_id: int, employee_email: str) -> Dict:
    for req in LEAVE_REQUESTS:
        if req['id'] == request_id and req['employee'] == employee_email:
            if req['status'] == 'PENDING':
                req['status'] = 'CANCELLED'
                return {'status': 'CANCELLED', 'request': req}
            else:
                return {'error': 'Cannot cancel approved/rejected request.'}
    return {'error': 'Request not found.'}

if __name__ == "__main__":
    print("Modify leave request 1:", modify_leave(1, 'alice@company.com', '2024-06-11', '2024-06-13'))
    print("Cancel leave request 1:", cancel_leave(1, 'alice@company.com'))
    print("Try to modify approved leave request 2:", modify_leave(2, 'alice@company.com', '2024-06-16', '2024-06-17'))
