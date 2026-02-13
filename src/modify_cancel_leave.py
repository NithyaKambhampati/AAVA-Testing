"""
Modify or Cancel Leave Requests
As an employee, I want to modify or cancel leave requests before approval, so that I can adjust my plans as needed.
"""
from datetime import datetime

def modify_leave_request(leave_request, new_start_date, new_end_date, new_reason=None):
    if leave_request['status'] != 'pending':
        return {'status': 'error', 'message': 'Cannot modify after approval'}
    leave_request['start'] = new_start_date.strftime('%Y-%m-%d')
    leave_request['end'] = new_end_date.strftime('%Y-%m-%d')
    if new_reason:
        leave_request['reason'] = new_reason
    leave_request['modified'] = True
    return {'status': 'success', 'request': leave_request, 'message': 'Leave request modified and re-routed'}

def cancel_leave_request(leave_request):
    if leave_request['status'] != 'pending':
        return {'status': 'error', 'message': 'Cannot cancel after approval'}
    leave_request['status'] = 'cancelled'
    return {'status': 'success', 'request': leave_request, 'message': 'Leave request cancelled'}

# Example usage
if __name__ == '__main__':
    leave_request = {'employee_id': 'E123', 'manager_id': 'M456', 'type': 'casual', 'start': '2024-07-01', 'end': '2024-07-02', 'status': 'pending', 'reason': 'Vacation'}
    print(modify_leave_request(leave_request, datetime(2024,7,3), datetime(2024,7,4), 'Changed dates'))
    leave_request['status'] = 'pending'
    print(cancel_leave_request(leave_request))
