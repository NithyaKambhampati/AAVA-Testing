"""
Leave Application Module
- Allows employees to apply for leave, checks balance and date overlap
- Handles insufficient balance and overlapping dates
"""

from datetime import datetime
from typing import List, Dict

LEAVE_BALANCES = {
    'alice@company.com': {'CASUAL': 5, 'SICK': 2, 'EARNED': 10},
}
LEAVE_HISTORY = {
    'alice@company.com': [
        {'type': 'CASUAL', 'start': '2024-05-01', 'end': '2024-05-03', 'status': 'APPROVED'},
    ],
}

def is_date_overlap(email: str, start_date: str, end_date: str) -> bool:
    new_start = datetime.strptime(start_date, '%Y-%m-%d')
    new_end = datetime.strptime(end_date, '%Y-%m-%d')
    for leave in LEAVE_HISTORY.get(email, []):
        leave_start = datetime.strptime(leave['start'], '%Y-%m-%d')
        leave_end = datetime.strptime(leave['end'], '%Y-%m-%d')
        if leave['status'] in ('APPROVED', 'PENDING') and not (new_end < leave_start or new_start > leave_end):
            return True
    return False

def apply_leave(email: str, leave_type: str, start_date: str, end_date: str, reason: str = "") -> Dict:
    balances = LEAVE_BALANCES.get(email, {})
    days_requested = (datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days + 1
    if leave_type not in balances or balances[leave_type] < days_requested:
        return {'error': 'Insufficient leave balance.'}
    if is_date_overlap(email, start_date, end_date):
        return {'error': 'Leave dates overlap with existing request.'}
    # Simulate submission
    LEAVE_HISTORY[email].append({
        'type': leave_type,
        'start': start_date,
        'end': end_date,
        'status': 'PENDING',
        'reason': reason
    })
    return {'status': 'PENDING', 'message': 'Leave request submitted for approval.'}

if __name__ == "__main__":
    email = input("Email: ")
    leave_type = input("Leave Type (CASUAL/SICK/EARNED): ")
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    reason = input("Reason (optional): ")
    result = apply_leave(email, leave_type, start_date, end_date, reason)
    print(result)
