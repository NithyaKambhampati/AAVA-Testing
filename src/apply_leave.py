"""
Apply for Leave: Request Creation and Validation
User Story: As an employee, I want to apply for leave by selecting type, dates, and reason, so that I can submit leave requests for approval.
"""

from datetime import datetime
from typing import List, Dict, Optional

# Simulated data
EMPLOYEE_DETAILS = {
    'alice@org.com': {'leave_balance': {'Sick Leave': 8, 'Casual Leave': 5, 'Earned Leave': 12}},
}
LEAVE_TYPES = ['Sick Leave', 'Casual Leave', 'Earned Leave']
LEAVE_REQUESTS = []

def is_overlap(email: str, start_date: str, end_date: str) -> bool:
    for req in LEAVE_REQUESTS:
        if req['email'] == email and req['status'] in ['Pending', 'Approved']:
            req_start = datetime.strptime(req['start_date'], '%Y-%m-%d')
            req_end = datetime.strptime(req['end_date'], '%Y-%m-%d')
            new_start = datetime.strptime(start_date, '%Y-%m-%d')
            new_end = datetime.strptime(end_date, '%Y-%m-%d')
            if new_start <= req_end and req_start <= new_end:
                return True
    return False

def apply_leave(email: str, leave_type: str, start_date: str, end_date: str, reason: Optional[str] = None) -> Dict:
    # Validate leave type
    if leave_type not in LEAVE_TYPES:
        return {'success': False, 'error': 'Invalid leave type.'}
    # Validate dates
    try:
        sd = datetime.strptime(start_date, '%Y-%m-%d')
        ed = datetime.strptime(end_date, '%Y-%m-%d')
        if ed < sd:
            return {'success': False, 'error': 'End date cannot be before start date.'}
    except ValueError:
        return {'success': False, 'error': 'Invalid date format. Use YYYY-MM-DD.'}
    # Check for overlap
    if is_overlap(email, start_date, end_date):
        return {'success': False, 'error': 'Overlapping leave request exists.'}
    # Validate balance
    days_requested = (ed - sd).days + 1
    balance = EMPLOYEE_DETAILS.get(email, {}).get('leave_balance', {}).get(leave_type, 0)
    if days_requested > balance:
        return {'success': False, 'error': 'Insufficient leave balance.'}
    # Create request
    request = {
        'email': email,
        'leave_type': leave_type,
        'start_date': start_date,
        'end_date': end_date,
        'reason': reason or '',
        'status': 'Pending',
        'created_at': datetime.now().isoformat()
    }
    LEAVE_REQUESTS.append(request)
    return {'success': True, 'request': request}

if __name__ == "__main__":
    # Example: Valid leave application
    result = apply_leave('alice@org.com', 'Sick Leave', '2024-06-10', '2024-06-12', 'Medical reason')
    print(result)
    # Example: Invalid leave type
    print(apply_leave('alice@org.com', 'Holiday', '2024-06-10', '2024-06-12'))
    # Example: Overlapping
    print(apply_leave('alice@org.com', 'Sick Leave', '2024-06-11', '2024-06-13'))
    # Example: Insufficient balance
    print(apply_leave('alice@org.com', 'Casual Leave', '2024-06-10', '2024-06-20'))
