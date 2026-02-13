"""
Validate Leave Requests
As the system, I want to validate leave requests for sufficient balance and date conflicts, so that only eligible requests are processed.
"""
from datetime import datetime

def validate_leave_request(employee, leave_type, start_date, end_date):
    days = (end_date - start_date).days + 1
    # Check sufficient balance
    if leave_type not in employee.leave_balances:
        return {'status': 'error', 'message': 'Invalid leave type'}
    if employee.leave_balances[leave_type] < days:
        return {'status': 'error', 'message': 'Insufficient leave balance'}
    # Check for overlapping dates and holidays
    for leave in employee.leave_history:
        if leave['status'] in ['approved', 'pending']:
            existing_start = datetime.strptime(leave['start'], '%Y-%m-%d')
            existing_end = datetime.strptime(leave['end'], '%Y-%m-%d')
            if not (end_date < existing_start or start_date > existing_end):
                return {'status': 'error', 'message': 'Leave dates overlap with existing request'}
    # Check max leave period (example: 30 days)
    if days > 30:
        return {'status': 'error', 'message': 'Maximum allowed leave period exceeded'}
    # Check holiday calendar (example: holidays list)
    holidays = ['2024-07-04', '2024-12-25']
    for i in range(days):
        day = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
        if day in holidays:
            return {'status': 'error', 'message': 'Leave includes holidays/non-working days'}
    return {'status': 'success', 'message': 'Leave request is valid'}

# Example usage
if __name__ == '__main__':
    from view_personal_details import Employee
    from datetime import datetime, timedelta
    leave_balances = {'casual': 8, 'sick': 5, 'earned': 12}
    leave_history = [
        {'type': 'casual', 'start': '2024-05-01', 'end': '2024-05-02', 'status': 'approved'},
        {'type': 'sick', 'start': '2024-06-10', 'end': '2024-06-11', 'status': 'rejected'}
    ]
    emp = Employee('E123', 'John Doe', leave_balances, leave_history)
    result = validate_leave_request(emp, 'casual', datetime(2024, 7, 1), datetime(2024, 7, 2))
    print(result)
