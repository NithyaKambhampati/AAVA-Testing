"""
Leave Validation Module
- Validates leave balance and overlapping dates
- Used by Leave Application workflow
"""

from datetime import datetime
from typing import List, Dict

def validate_leave_balance(balances: Dict[str, int], leave_type: str, days_requested: int) -> bool:
    return balances.get(leave_type, 0) >= days_requested

def validate_date_overlap(leave_history: List[Dict], start_date: str, end_date: str) -> bool:
    new_start = datetime.strptime(start_date, '%Y-%m-%d')
    new_end = datetime.strptime(end_date, '%Y-%m-%d')
    for leave in leave_history:
        leave_start = datetime.strptime(leave['start'], '%Y-%m-%d')
        leave_end = datetime.strptime(leave['end'], '%Y-%m-%d')
        if leave['status'] in ('APPROVED', 'PENDING') and not (new_end < leave_start or new_start > leave_end):
            return False  # Overlap found
    return True

# Example usage
if __name__ == "__main__":
    balances = {'CASUAL': 5, 'SICK': 2, 'EARNED': 10}
    leave_history = [
        {'type': 'CASUAL', 'start': '2024-05-01', 'end': '2024-05-03', 'status': 'APPROVED'},
    ]
    leave_type = 'CASUAL'
    start_date = '2024-05-02'
    end_date = '2024-05-04'
    days_requested = 3
    if not validate_leave_balance(balances, leave_type, days_requested):
        print('Insufficient leave balance.')
    elif not validate_date_overlap(leave_history, start_date, end_date):
        print('Leave dates overlap with existing request.')
    else:
        print('Validation passed.')
