"""
Automatic Leave Balance Updates
User Story: As an employee, I want my leave balance to update automatically when requests are approved, so that my available leave reflects actual usage.
"""

from typing import Dict

# Simulated leave balances and requests
EMPLOYEE_BALANCES = {
    'alice@org.com': {'Sick Leave': 8, 'Casual Leave': 5, 'Earned Leave': 12},
}
LEAVE_REQUESTS = [
    {'request_id': 1, 'email': 'alice@org.com', 'leave_type': 'Sick Leave', 'start_date': '2024-06-10', 'end_date': '2024-06-12', 'status': 'Approved'},
    {'request_id': 2, 'email': 'alice@org.com', 'leave_type': 'Casual Leave', 'start_date': '2024-07-01', 'end_date': '2024-07-02', 'status': 'Rejected'},
    {'request_id': 3, 'email': 'alice@org.com', 'leave_type': 'Earned Leave', 'start_date': '2024-07-10', 'end_date': '2024-07-12', 'status': 'Cancelled'},
]

def update_leave_balances(email: str) -> Dict:
    updated_balances = EMPLOYEE_BALANCES.get(email, {}).copy()
    for req in LEAVE_REQUESTS:
        if req['email'] == email and req['status'] == 'Approved':
            days = (int(req['end_date'][-2:]) - int(req['start_date'][-2:])) + 1
            leave_type = req['leave_type']
            updated_balances[leave_type] = max(0, updated_balances.get(leave_type, 0) - days)
    return updated_balances

if __name__ == "__main__":
    email = 'alice@org.com'
    print(f"Balances before update: {EMPLOYEE_BALANCES[email]}")
    updated = update_leave_balances(email)
    print(f"Balances after update: {updated}")
