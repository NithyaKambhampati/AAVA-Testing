# Employee Leave Application and Validation
# Implements leave request creation, validation (balance, dates, overlaps), and routing for approval

from datetime import date

class LeaveRequest:
 def __init__(self, employee_id, leave_type, start_date, end_date, reason=None):
 self.employee_id = employee_id
 self.leave_type = leave_type
 self.start_date = start_date
 self.end_date = end_date
 self.reason = reason
 self.status = 'pending'

class LeaveManager:
 def __init__(self, leave_balances, configured_leave_types, leave_requests):
 self.leave_balances = leave_balances # employee_id -> {leave_type: balance}
 self.configured_leave_types = configured_leave_types # set of leave types
 self.leave_requests = leave_requests # list of LeaveRequest

 def validate_leave(self, employee_id, leave_type, start_date, end_date):
 # Check leave type configuration
 if leave_type not in self.configured_leave_types:
 return False, 'Leave type not configured'
 # Check date validity
 if end_date < start_date:
 return False, 'Invalid date range'
 # Check balance
 balance = self.leave_balances.get(employee_id, {}).get(leave_type, 0)
 days_requested = (end_date - start_date).days + 1
 if balance < days_requested:
 return False, 'Insufficient leave balance'
 # Check for overlapping requests
 for lr in self.leave_requests:
 if lr.employee_id == employee_id and lr.status in ['pending', 'approved']:
 if not (end_date < lr.start_date or start_date > lr.end_date):
 return False, 'Overlapping leave request'
 return True, ''

 def apply_leave(self, employee_id, leave_type, start_date, end_date, reason=None):
 valid, msg = self.validate_leave(employee_id, leave_type, start_date, end_date)
 if not valid:
 return {'success': False, 'error': msg}
 lr = LeaveRequest(employee_id, leave_type, start_date, end_date, reason)
 self.leave_requests.append(lr)
 # Route for approval (placeholder)
 return {'success': True, 'request': lr}

# Example usage:
leave_balances = {'alice': {'casual': 5, 'sick': 2}}
configured_leave_types = {'casual', 'sick', 'earned'}
leave_requests = []
lm = LeaveManager(leave_balances, configured_leave_types, leave_requests)
result = lm.apply_leave('alice', 'casual', date(2024,6,10), date(2024,6,12), 'Vacation')
print(result)
