"""
System Integration with HR/Employee Systems
User Story: As an HR/Admin, I want the LMS to integrate with existing HR and employee systems, so that leave balances, employee details, and policies are kept up-to-date and consistent.
"""

from typing import Dict, Any
import time

# Simulated HR system API
HR_SYSTEM = {
    'employees': {
        'alice@org.com': {'name': 'Alice', 'leave_balance': 12, 'policy': 'Standard'},
        'bob@org.com': {'name': 'Bob', 'leave_balance': 10, 'policy': 'Standard'},
    },
    'policies': {'Standard': {'accrual': '1 per month'}},
}

LMS_EMPLOYEES = {}
LMS_POLICIES = {}


def sync_from_hr_system():
    # Simulate periodic sync (every 24 hours)
    global LMS_EMPLOYEES, LMS_POLICIES
    LMS_EMPLOYEES = HR_SYSTEM['employees'].copy()
    LMS_POLICIES = HR_SYSTEM['policies'].copy()
    print("LMS data synced from HR system.")


def sync_to_hr_system():
    # Simulate updating HR system with LMS changes
    HR_SYSTEM['employees'].update(LMS_EMPLOYEES)
    HR_SYSTEM['policies'].update(LMS_POLICIES)
    print("HR system updated from LMS.")

if __name__ == "__main__":
    sync_from_hr_system()
    print("LMS Employees:", LMS_EMPLOYEES)
    print("LMS Policies:", LMS_POLICIES)
    # Simulate change in LMS
    LMS_EMPLOYEES['alice@org.com']['leave_balance'] = 9
    sync_to_hr_system()
    print("HR System Employees:", HR_SYSTEM['employees'])
