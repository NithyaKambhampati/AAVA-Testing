"""
Employee Leave Application
Allows employees to apply for leave with type, dates, and reason. Validates balance and dates.
"""
from datetime import datetime

class LeaveType:
 CASUAL = 'casual'
 SICK = 'sick'
 EARNED = 'earned'
 CUSTOM = 'custom'

class LeaveApplication:
 def __init__(self, employee_id, data_source):
 self.employee_id = employee_id
 self.data_source = data_source # Should provide balances, check overlaps, etc.

 def is_valid_dates(self, start_date, end_date):
 return start_date <= end_date

 def has_sufficient_balance(self, leave_type, days):
 balances = self.data_source.get_leave_balances(self.employee_id)
 return balances.get(leave_type, 0) >= days

 def is_overlapping(self, start_date, end_date):
 history = self.data_source.get_leave_history(self.employee_id)
 for leave in history:
 if leave['status'] in ['approved', 'pending']:
 # Check for overlap
 if not (end_date < leave['start_date'] or start_date > leave['end_date']):
 return True
 return False

 def apply(self, leave_type, start_date, end_date, reason=None):
 if not self.is_valid_dates(start_date, end_date):
 return {'success': False, 'error': 'Invalid date range'}
 days = (end_date - start_date).days + 1
 if not self.has_sufficient_balance(leave_type, days):
 return {'success': False, 'error': 'Insufficient leave balance'}
 if self.is_overlapping(start_date, end_date):
 return {'success': False, 'error': 'Overlapping leave request'}
 # All validations passed, submit request
 self.data_source.submit_leave_request(self.employee_id, leave_type, start_date, end_date, reason)
 return {'success': True, 'message': 'Leave request submitted'}

# Example usage (assuming data_source implements required methods):
# app = LeaveApplication('emp001', data_source)
# result = app.apply('casual', datetime(2024,7,1), datetime(2024,7,3), 'Vacation')
# print(result)
