"""
Integration with HR/Employee Systems
As an HR/Admin, I want the LMS to integrate with existing HR/employee systems so that data sync is maintained and user information is accurate.
"""

from typing import Dict
import random

HR_SYSTEM_DB = {
    'employee1': {'name': 'Alice', 'leave_balance': {'casual': 7, 'sick': 2}},
}
LMS_DB = {
    'employee1': {'name': 'Alice', 'leave_balance': {'casual': 5, 'sick': 3}},
}

class IntegrationError(Exception):
    pass

def sync_hr_to_lms(employee_id: str):
    hr_data = HR_SYSTEM_DB.get(employee_id)
    if not hr_data:
        raise IntegrationError('HR data not found.')
    # Simulate sync failure
    if random.choice([True, False]):
        LMS_DB[employee_id]['leave_balance'] = hr_data['leave_balance']
        print(f"Synced HR data for {employee_id} to LMS.")
    else:
        print(f"HR sync failed for {employee_id}.")
        raise IntegrationError('HR sync failure.')

def sync_lms_to_hr(employee_id: str):
    lms_data = LMS_DB.get(employee_id)
    if not lms_data:
        raise IntegrationError('LMS data not found.')
    HR_SYSTEM_DB[employee_id]['leave_balance'] = lms_data['leave_balance']
    print(f"Synced LMS data for {employee_id} to HR system.")

# Example usage
if __name__ == '__main__':
    try:
        sync_hr_to_lms('employee1')
    except IntegrationError as e:
        print(str(e))
    sync_lms_to_hr('employee1')
    print('HR_SYSTEM_DB:', HR_SYSTEM_DB)
    print('LMS_DB:', LMS_DB)
