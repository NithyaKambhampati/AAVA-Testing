"""
Employee Dashboard: Leave Overview and Application
As an employee, I want to view my personal details, leave balances, and history, and apply for various types of leave so that I can manage my leave efficiently.
"""

from typing import List, Dict, Optional
import datetime

LEAVE_TYPES = ['casual', 'sick', 'earned', 'custom']
HOLIDAYS = [datetime.date(2024, 12, 25), datetime.date(2024, 1, 1)]

EMPLOYEE_DB = {
    'employee1': {
        'personal_details': {'name': 'Alice', 'id': 'E001'},
        'leave_balance': {'casual': 5, 'sick': 3, 'earned': 10, 'custom': 2},
        'leave_history': []
    }
}

class LeaveApplicationError(Exception):
    pass

def view_dashboard(employee_id: str) -> Dict:
    employee = EMPLOYEE_DB.get(employee_id)
    if employee:
        return {
            'personal_details': employee['personal_details'],
            'leave_balance': employee['leave_balance'],
            'leave_history': employee['leave_history']
        }
    else:
        raise LeaveApplicationError('Employee not found.')

def validate_leave_application(employee_id: str, leave_type: str, start_date: datetime.date, end_date: datetime.date) -> Optional[str]:
    employee = EMPLOYEE_DB.get(employee_id)
    if leave_type not in LEAVE_TYPES:
        return 'Invalid leave type.'
    if start_date > end_date:
        return 'Start date must be before end date.'
    if start_date in HOLIDAYS or end_date in HOLIDAYS:
        return 'Leave dates fall on organization holiday.'
    # Check balance
    days_requested = (end_date - start_date).days + 1
    if employee['leave_balance'][leave_type] < days_requested:
        return 'Insufficient leave balance.'
    # Check overlap
    for req in employee['leave_history']:
        if req['status'] == 'approved':
            if not (end_date < req['start_date'] or start_date > req['end_date']):
                return 'Leave dates overlap with existing approved leave.'
    return None

def apply_for_leave(employee_id: str, leave_type: str, start_date: datetime.date, end_date: datetime.date, reason: str) -> str:
    validation_msg = validate_leave_application(employee_id, leave_type, start_date, end_date)
    if validation_msg:
        raise LeaveApplicationError(validation_msg)
    EMPLOYEE_DB[employee_id]['leave_history'].append({
        'leave_type': leave_type,
        'start_date': start_date,
        'end_date': end_date,
        'reason': reason,
        'status': 'pending'
    })
    return 'Leave request submitted for approval.'

def cancel_leave_request(employee_id: str, request_index: int) -> str:
    history = EMPLOYEE_DB[employee_id]['leave_history']
    req = history[request_index]
    if req['status'] == 'pending':
        req['status'] = 'cancelled'
        return 'Leave request cancelled.'
    else:
        return 'Cannot cancel approved leave. Contact manager.'

# Example usage
if __name__ == '__main__':
    dashboard = view_dashboard('employee1')
    print('Dashboard:', dashboard)
    try:
        msg = apply_for_leave('employee1', 'casual', datetime.date(2024, 7, 10), datetime.date(2024, 7, 12), 'Family event')
        print(msg)
    except LeaveApplicationError as e:
        print(str(e))
