"""
HR/Admin Configuration and Reporting
As an HR/Admin user, I want to configure leave types, policies, accrual rules, and holiday calendars, and view leave reports so that I can manage organizational leave settings and monitor leave trends.
"""

from typing import Dict, List
import datetime

LEAVE_TYPES = {'casual': {'accrual_rule': 'monthly', 'policy_details': 'max 12/year'},
               'sick': {'accrual_rule': 'monthly', 'policy_details': 'max 6/year'}}
HOLIDAY_CALENDAR = [datetime.date(2024, 12, 25), datetime.date(2024, 1, 1)]

LEAVE_REPORTS = [
    {'employee_id': 'employee1', 'leave_type': 'casual', 'days_taken': 3, 'status': 'approved'},
    {'employee_id': 'employee1', 'leave_type': 'sick', 'days_taken': 2, 'status': 'approved'}
]

class AdminConfigError(Exception):
    pass

def configure_leave_type(leave_type: str, accrual_rule: str, policy_details: str):
    LEAVE_TYPES[leave_type] = {'accrual_rule': accrual_rule, 'policy_details': policy_details}

def configure_holiday_calendar(date: datetime.date, description: str):
    HOLIDAY_CALENDAR.append(date)

def view_leave_reports() -> List[Dict]:
    return LEAVE_REPORTS

# Example usage
if __name__ == '__main__':
    configure_leave_type('earned', 'yearly', 'max 15/year')
    configure_holiday_calendar(datetime.date(2024, 8, 15), 'Independence Day')
    reports = view_leave_reports()
    print('Leave reports:', reports)
    print('Leave types:', LEAVE_TYPES)
    print('Holiday calendar:', HOLIDAY_CALENDAR)
