import datetime

class LeaveApplication:
    def __init__(self, employee_id, leave_balance):
        self.employee_id = employee_id
        self.leave_balance = leave_balance
        self.leave_requests = []

    def apply_for_leave(self, start_date_str, end_date_str):
        try:
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return {'success': False, 'message': 'Invalid date format. Use YYYY-MM-DD.'}

        today = datetime.date.today()
        if start_date < today or end_date < today:
            return {'success': False, 'message': 'Past dates are not allowed.'}
        if end_date < start_date:
            return {'success': False, 'message': 'End date cannot be before start date.'}

        days_requested = (end_date - start_date).days + 1
        if days_requested > self.leave_balance:
            return {'success': False, 'message': 'Insufficient leave balance.'}

        # Store leave request
        leave_request = {
            'employee_id': self.employee_id,
            'start_date': start_date_str,
            'end_date': end_date_str,
            'days_requested': days_requested,
            'status': 'Submitted'
        }
        self.leave_requests.append(leave_request)
        self.leave_balance -= days_requested

        return {'success': True, 'message': f'Leave applied successfully for {days_requested} day(s).', 'leave_request': leave_request}

# Example usage:
if __name__ == "__main__":
    employee = LeaveApplication(employee_id=1234, leave_balance=10)
    result = employee.apply_for_leave('2024-07-01', '2024-07-05')
    print(result['message'])
    if result['success']:
        print('Leave details:', result['leave_request'])
