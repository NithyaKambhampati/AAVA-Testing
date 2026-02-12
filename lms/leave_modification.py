"""
Employee Leave Modification and Cancellation
Allows employees to cancel or modify a pending leave request. Not allowed after approval.
"""
from datetime import datetime

class LeaveModification:
 def __init__(self, employee_id, data_source):
 self.employee_id = employee_id
 self.data_source = data_source # Should provide leave request lookup and update

 def cancel_request(self, request_id):
 leave = self.data_source.get_leave_request(self.employee_id, request_id)
 if leave and leave['status'] == 'pending':
 self.data_source.update_leave_request(request_id, {'status': 'cancelled'})
 self.data_source.notify_manager(leave['manager_id'], f"Leave request {request_id} cancelled by employee.")
 return {'success': True, 'message': 'Leave request cancelled and manager notified'}
 return {'success': False, 'error': 'Cannot cancel approved or non-existent request'}

 def modify_request(self, request_id, new_start, new_end, new_reason=None):
 leave = self.data_source.get_leave_request(self.employee_id, request_id)
 if leave and leave['status'] == 'pending':
 if new_start > new_end:
 return {'success': False, 'error': 'Invalid date range'}
 self.data_source.update_leave_request(request_id, {
 'start_date': new_start,
 'end_date': new_end,
 'reason': new_reason,
 'status': 'pending', # restart approval
 })
 self.data_source.notify_manager(leave['manager_id'], f"Leave request {request_id} modified by employee.")
 return {'success': True, 'message': 'Leave request modified and manager notified'}
 return {'success': False, 'error': 'Cannot modify approved or non-existent request'}

# Example usage (assuming data_source implements required methods):
# mod = LeaveModification('emp001', data_source)
# print(mod.cancel_request('req123'))
# print(mod.modify_request('req123', datetime(2024,7,10), datetime(2024,7,12), 'Changed dates'))
