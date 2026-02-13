"""
HR/Admin Configuration: Leave Types, Policies, Accrual, and Holidays
User Story: As an HR/Admin, I want to configure leave types, policies, accrual rules, and holiday calendars, so that the system aligns with organizational standards and provides accurate leave calculations.
"""

from typing import Dict, List
from datetime import datetime

# Simulated config data
LEAVE_TYPES = ['Sick Leave', 'Casual Leave', 'Earned Leave']
LEAVE_POLICIES = {'max_consecutive_days': 10}
ACCRUAL_RULES = {'Earned Leave': '1 day per month'}
HOLIDAY_CALENDAR = ['2024-01-01', '2024-12-25']
AUDIT_LOG = []

# Only HR/Admin can configure
HR_ADMINS = ['carol@org.com']

def configure_leave_type(admin_email: str, leave_type: str) -> bool:
    if admin_email not in HR_ADMINS:
        return False
    if leave_type not in LEAVE_TYPES:
        LEAVE_TYPES.append(leave_type)
        AUDIT_LOG.append({'action': 'Add Leave Type', 'type': leave_type, 'by': admin_email, 'timestamp': datetime.now().isoformat()})
        return True
    return False

def update_policy(admin_email: str, policy_key: str, value) -> bool:
    if admin_email not in HR_ADMINS:
        return False
    LEAVE_POLICIES[policy_key] = value
    AUDIT_LOG.append({'action': 'Update Policy', 'policy': policy_key, 'value': value, 'by': admin_email, 'timestamp': datetime.now().isoformat()})
    return True

def add_holiday(admin_email: str, date_str: str) -> bool:
    if admin_email not in HR_ADMINS:
        return False
    if date_str not in HOLIDAY_CALENDAR:
        HOLIDAY_CALENDAR.append(date_str)
        AUDIT_LOG.append({'action': 'Add Holiday', 'date': date_str, 'by': admin_email, 'timestamp': datetime.now().isoformat()})
        return True
    return False

if __name__ == "__main__":
    print(configure_leave_type('carol@org.com', 'Comp Off'))
    print(update_policy('carol@org.com', 'max_consecutive_days', 15))
    print(add_holiday('carol@org.com', '2024-08-15'))
    print(AUDIT_LOG)
