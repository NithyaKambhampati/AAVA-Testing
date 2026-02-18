"""
Leave Balance Management
As an employee, I want my leave balance to be automatically updated only upon manager approval so that my available leave is always accurate.
"""

from typing import Dict
import datetime

EMPLOYEE_LEAVE_BALANCE = {
    'employee1': {'casual': 5, 'sick': 3, 'earned': 10, 'custom': 2}
}

LEAVE_REQUESTS = [
    {'employee_id': 'employee1', 'leave_type': 'casual', 'start_date': datetime.date(2024, 7, 10), 'end_date': datetime.date(2024, 7, 12), 'status': 'approved'},
    {'employee_id': 'employee1', 'leave_type': 'sick', 'start_date': datetime.date(2024, 7, 15), 'end_date': datetime.date(2024, 7, 16), 'status': 'rejected'}
]

def update_leave_balance_on_approval(employee_id: str, leave_type: str, start_date: datetime.date, end_date: datetime.date, status: str):
    days = (end_date - start_date).days + 1
    if status == 'approved':
        EMPLOYEE_LEAVE_BALANCE[employee_id][leave_type] -= days
    # Rejected or cancelled requests do not affect balance

def get_leave_balance(employee_id: str) -> Dict[str, int]:
    return EMPLOYEE_LEAVE_BALANCE.get(employee_id, {})

# Example usage
if __name__ == '__main__':
    for req in LEAVE_REQUESTS:
        update_leave_balance_on_approval(req['employee_id'], req['leave_type'], req['start_date'], req['end_date'], req['status'])
    print('Leave balance:', get_leave_balance('employee1'))
