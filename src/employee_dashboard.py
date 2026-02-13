"""
Employee Dashboard Module
- Displays personal details, leave balances, and leave history for logged-in employees
"""

from typing import List, Dict

# Simulated leave history and balances
LEAVE_BALANCES = {
    'alice@company.com': {'CASUAL': 5, 'SICK': 2, 'EARNED': 10},
    'bob@company.com': {'CASUAL': 3, 'SICK': 1, 'EARNED': 8},
}
LEAVE_HISTORY = {
    'alice@company.com': [
        {'type': 'CASUAL', 'start': '2024-05-01', 'end': '2024-05-03', 'status': 'APPROVED'},
        {'type': 'SICK', 'start': '2024-04-10', 'end': '2024-04-12', 'status': 'REJECTED'}
    ],
    'bob@company.com': [
        {'type': 'EARNED', 'start': '2024-03-15', 'end': '2024-03-20', 'status': 'APPROVED'}
    ],
}

EMPLOYEE_DETAILS = {
    'alice@company.com': {'name': 'Alice', 'department': 'HR'},
    'bob@company.com': {'name': 'Bob', 'department': 'Engineering'},
}

def get_dashboard(email: str) -> Dict:
    details = EMPLOYEE_DETAILS.get(email, {})
    balances = LEAVE_BALANCES.get(email, {})
    history = LEAVE_HISTORY.get(email, [])
    return {
        'personal_details': details,
        'leave_balances': balances,
        'leave_history': history
    }

if __name__ == "__main__":
    email = input("Enter your email: ")
    dashboard = get_dashboard(email)
    if dashboard['personal_details']:
        print("Personal Details:", dashboard['personal_details'])
        print("Leave Balances:", dashboard['leave_balances'])
        print("Leave History:")
        for record in dashboard['leave_history']:
            print(record)
    else:
        print("No dashboard data found for this user.")
