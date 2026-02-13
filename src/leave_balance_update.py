"""
Leave Balance Update Module
- Updates leave balances for approved requests
- Ensures rejected/cancelled requests do not affect balances
"""

from typing import Dict

LEAVE_BALANCES = {'alice@company.com': {'CASUAL': 5, 'SICK': 2, 'EARNED': 10}}

LEAVE_REQUESTS = [
    {'id': 1, 'employee': 'alice@company.com', 'type': 'CASUAL', 'start': '2024-06-10', 'end': '2024-06-12', 'status': 'APPROVED'},
    {'id': 2, 'employee': 'alice@company.com', 'type': 'SICK', 'start': '2024-06-15', 'end': '2024-06-16', 'status': 'REJECTED'},
]

def update_leave_balance(request_id: int):
    for req in LEAVE_REQUESTS:
        if req['id'] == request_id:
            if req['status'] == 'APPROVED':
                days = (int(req['end'][-2:]) - int(req['start'][-2:]) + 1)
                LEAVE_BALANCES[req['employee']][req['type']] -= days
                return {'status': 'UPDATED', 'balance': LEAVE_BALANCES[req['employee']][req['type']]}
            else:
                return {'status': 'NO_CHANGE', 'balance': LEAVE_BALANCES[req['employee']][req['type']]}
    return {'error': 'Request not found.'}

if __name__ == "__main__":
    print("Update leave balance for request 1:", update_leave_balance(1))
    print("Update leave balance for request 2:", update_leave_balance(2))
