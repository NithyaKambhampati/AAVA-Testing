"""
Approval Workflow Module
- Managers review, approve/reject leave requests
- Handles escalation if manager is absent
- Notifies employee and updates leave balance if approved
"""

from typing import Dict, List

LEAVE_REQUESTS = [
    {'id': 1, 'employee': 'alice@company.com', 'type': 'CASUAL', 'start': '2024-06-10', 'end': '2024-06-12', 'status': 'PENDING', 'manager': 'bob@company.com', 'reason': 'Vacation'},
]
LEAVE_BALANCES = {'alice@company.com': {'CASUAL': 5, 'SICK': 2, 'EARNED': 10}}

MANAGER_ABSENCE = {'bob@company.com': False}  # False means present

NOTIFICATIONS = []


def approve_leave(request_id: int, manager_email: str, comments: str = "") -> Dict:
    for req in LEAVE_REQUESTS:
        if req['id'] == request_id and req['manager'] == manager_email and req['status'] == 'PENDING':
            req['status'] = 'APPROVED'
            LEAVE_BALANCES[req['employee']][req['type']] -= (
                (int(req['end'][-2:]) - int(req['start'][-2:]) + 1)
            )
            NOTIFICATIONS.append({'to': req['employee'], 'message': f"Leave request approved. {comments}"})
            return {'status': 'APPROVED', 'message': 'Leave approved.'}
    return {'error': 'Request not found or already processed.'}

def reject_leave(request_id: int, manager_email: str, comments: str = "") -> Dict:
    for req in LEAVE_REQUESTS:
        if req['id'] == request_id and req['manager'] == manager_email and req['status'] == 'PENDING':
            req['status'] = 'REJECTED'
            NOTIFICATIONS.append({'to': req['employee'], 'message': f"Leave request rejected. {comments}"})
            return {'status': 'REJECTED', 'message': 'Leave rejected.'}
    return {'error': 'Request not found or already processed.'}

def escalate_request(request_id: int) -> Dict:
    for req in LEAVE_REQUESTS:
        if req['id'] == request_id and req['status'] == 'PENDING':
            if MANAGER_ABSENCE.get(req['manager'], False):
                req['manager'] = 'carol@company.com'  # Escalate to HR
                NOTIFICATIONS.append({'to': req['employee'], 'message': 'Request escalated to HR.'})
                return {'status': 'ESCALATED', 'message': 'Request escalated.'}
    return {'error': 'No escalation needed.'}

if __name__ == "__main__":
    print("Approval Workflow Demo:")
    print("Approve leave:", approve_leave(1, 'bob@company.com', 'Enjoy your vacation!'))
    print("Reject leave:", reject_leave(1, 'bob@company.com', 'Cannot approve at this time.'))
    MANAGER_ABSENCE['bob@company.com'] = True
    print("Escalate (manager absent):", escalate_request(1))
    print("Notifications:", NOTIFICATIONS)
