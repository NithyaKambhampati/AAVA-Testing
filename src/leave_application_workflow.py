"""
Leave Application Workflow and Manager Approval
As a manager, I want to review, approve, or reject leave requests from my team so that I can ensure appropriate leave coverage and compliance.
"""

from typing import Dict, List
import datetime

TEAM_LEAVE_REQUESTS = [
    {'employee_id': 'employee1', 'leave_type': 'casual', 'start_date': datetime.date(2024, 7, 10), 'end_date': datetime.date(2024, 7, 12), 'reason': 'Family event', 'status': 'pending', 'manager_comment': ''}
]

class ManagerActionError(Exception):
    pass

def view_pending_requests(manager_id: str) -> List[Dict]:
    # For demo, return all pending requests
    return [req for req in TEAM_LEAVE_REQUESTS if req['status'] == 'pending']

def approve_leave_request(request_index: int, manager_id: str, comment: str) -> str:
    req = TEAM_LEAVE_REQUESTS[request_index]
    if req['status'] != 'pending':
        raise ManagerActionError('Request is not pending.')
    req['status'] = 'approved'
    req['manager_comment'] = comment
    # Notify employee (mock)
    print(f"Notification: Leave approved for {req['employee_id']}. Comment: {comment}")
    return 'Leave approved.'

def reject_leave_request(request_index: int, manager_id: str, comment: str) -> str:
    req = TEAM_LEAVE_REQUESTS[request_index]
    if req['status'] != 'pending':
        raise ManagerActionError('Request is not pending.')
    req['status'] = 'rejected'
    req['manager_comment'] = comment
    # Notify employee (mock)
    print(f"Notification: Leave rejected for {req['employee_id']}. Comment: {comment}")
    return 'Leave rejected.'

# Example usage
if __name__ == '__main__':
    pending = view_pending_requests('manager1')
    print('Pending requests:', pending)
    try:
        msg = approve_leave_request(0, 'manager1', 'Approved, ensure coverage')
        print(msg)
    except ManagerActionError as e:
        print(str(e))
