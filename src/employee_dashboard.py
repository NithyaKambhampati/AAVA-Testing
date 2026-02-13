"""
Employee Dashboard: View Details, Leave Balances, and History
User Story: As an employee, I want to view my personal details, available leave balances, and leave history, so that I can track my leave status and plan accordingly.
"""

from typing import List, Dict

# Simulated leave data
EMPLOYEE_LEAVE_HISTORY = {
    'alice@org.com': [
        {'type': 'Sick Leave', 'start_date': '2024-04-10', 'end_date': '2024-04-12', 'status': 'Approved'},
        {'type': 'Casual Leave', 'start_date': '2024-05-01', 'end_date': '2024-05-01', 'status': 'Rejected'},
    ]
}
EMPLOYEE_DETAILS = {
    'alice@org.com': {'name': 'Alice', 'leave_balance': {'Sick Leave': 8, 'Casual Leave': 5, 'Earned Leave': 12}},
}

def get_employee_dashboard(email: str) -> Dict:
    """
    Returns personal details, leave balances, and leave history for the employee.
    """
    details = EMPLOYEE_DETAILS.get(email, {'name': '', 'leave_balance': {}})
    history = EMPLOYEE_LEAVE_HISTORY.get(email, [])
    return {
        'personal_details': details,
        'leave_history': history
    }

if __name__ == "__main__":
    email = 'alice@org.com'
    dashboard = get_employee_dashboard(email)
    print(f"Personal Details: {dashboard['personal_details']}")
    if dashboard['leave_history']:
        print("Leave History:")
        for record in dashboard['leave_history']:
            print(record)
    else:
        print("No leave history found.")
