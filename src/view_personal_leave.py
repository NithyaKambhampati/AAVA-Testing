# View Personal Leave Details and History
# Implements dashboard for employee to see details, balances, and leave history

class Employee:
 def __init__(self, employee_id, name, details):
 self.employee_id = employee_id
 self.name = name
 self.details = details # dict with personal info

class LeaveHistory:
 def __init__(self, leave_requests):
 self.leave_requests = leave_requests # list of LeaveRequest

 def get_history(self, employee_id):
 return [lr for lr in self.leave_requests if lr.employee_id == employee_id]

 def get_balances(self, employee_id, leave_balances):
 return leave_balances.get(employee_id, {})

 def get_dashboard(self, employee_id, leave_balances):
 history = self.get_history(employee_id)
 balances = self.get_balances(employee_id, leave_balances)
 return {
 'personal_details': {'employee_id': employee_id},
 'leave_balances': balances,
 'leave_history': [vars(lr) for lr in history]
 }

# Example usage:
leave_balances = {'alice': {'casual': 5, 'sick': 2}}
leave_requests = [] # Add LeaveRequest objects as needed
lh = LeaveHistory(leave_requests)
dash = lh.get_dashboard('alice', leave_balances)
print(dash)
