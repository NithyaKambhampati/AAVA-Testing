# Leave Request Modification and Cancellation (Pre-Approval)
# Allows employees to modify or cancel pending leave requests; restricts changes post-approval

class LeaveRequest:
 def __init__(self, employee_id, leave_type, start_date, end_date, reason=None):
 self.employee_id = employee_id
 self.leave_type = leave_type
 self.start_date = start_date
 self.end_date = end_date
 self.reason = reason
 self.status = 'pending'

class LeaveRequestModifier:
 def __init__(self, leave_requests):
 self.leave_requests = leave_requests # list of LeaveRequest

 def modify_request(self, employee_id, request_id, new_start, new_end, new_reason=None):
 lr = self._find_request(employee_id, request_id)
 if lr is None:
 return {'success': False, 'error': 'Request not found'}
 if lr.status != 'pending':
 return {'success': False, 'error': 'Cannot modify approved/rejected request'}
 lr.start_date = new_start
 lr.end_date = new_end
 lr.reason = new_reason
 lr.status = 'pending' # Re-initiate approval
 return {'success': True, 'request': lr}

 def cancel_request(self, employee_id, request_id):
 lr = self._find_request(employee_id, request_id)
 if lr is None:
 return {'success': False, 'error': 'Request not found'}
 if lr.status != 'pending':
 return {'success': False, 'error': 'Cannot cancel approved/rejected request'}
 lr.status = 'cancelled'
 return {'success': True, 'request': lr}

 def _find_request(self, employee_id, request_id):
 for lr in self.leave_requests:
 if lr.employee_id == employee_id and id(lr) == request_id:
 return lr
 return None

# Example usage:
leave_requests = [] # Add LeaveRequest objects as needed
modifier = LeaveRequestModifier(leave_requests)
# Suppose we have a request:
lr = LeaveRequest('alice', 'casual', '2024-06-10', '2024-06-12', 'Vacation')
leave_requests.append(lr)
req_id = id(lr)
print(modifier.modify_request('alice', req_id, '2024-06-11', '2024-06-13', 'Changed plans'))
print(modifier.cancel_request('alice', req_id))
