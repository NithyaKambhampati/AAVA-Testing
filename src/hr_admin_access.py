"""
HR/Admin Access and Configuration Module
- HR/Admin can configure leave types, policies, accrual rules, and holiday calendars
- Handles policy changes for in-process requests
"""

from typing import Dict, List

LEAVE_TYPES = {'CASUAL': {'max_days': 10}, 'SICK': {'max_days': 5}, 'EARNED': {'max_days': 15}}
POLICIES = {'CASUAL': {'carry_forward': True}, 'SICK': {'carry_forward': False}, 'EARNED': {'carry_forward': True}}
HOLIDAY_CALENDAR = ['2024-06-14', '2024-07-04']

IN_PROCESS_REQUESTS = [
    {'id': 1, 'employee': 'alice@company.com', 'type': 'CASUAL', 'start': '2024-06-10', 'end': '2024-06-12', 'status': 'PENDING'},
]


def update_leave_type(type_name: str, params: Dict):
    LEAVE_TYPES[type_name] = params
    return {'status': 'UPDATED', 'leave_types': LEAVE_TYPES}

def update_policy(type_name: str, policy: Dict):
    POLICIES[type_name] = policy
    return {'status': 'UPDATED', 'policies': POLICIES}

def update_holiday_calendar(date: str):
    HOLIDAY_CALENDAR.append(date)
    return {'status': 'UPDATED', 'calendar': HOLIDAY_CALENDAR}

def handle_policy_change_for_requests():
    # Example: apply new policy to in-process requests
    for req in IN_PROCESS_REQUESTS:
        if req['type'] in POLICIES:
            req['policy_applied'] = POLICIES[req['type']]
    return {'status': 'POLICY_APPLIED', 'requests': IN_PROCESS_REQUESTS}

if __name__ == "__main__":
    print(update_leave_type('CASUAL', {'max_days': 12}))
    print(update_policy('CASUAL', {'carry_forward': False}))
    print(update_holiday_calendar('2024-08-15'))
    print(handle_policy_change_for_requests())
