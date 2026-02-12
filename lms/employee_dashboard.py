"""
Employee Leave Dashboard
Allows employees to view their profile, leave balances, and leave history.
"""

class EmployeeDashboard:
 def __init__(self, employee_id, data_source):
 self.employee_id = employee_id
 self.data_source = data_source # Should provide profile, balances, history

 def get_profile(self):
 return self.data_source.get_profile(self.employee_id)

 def get_leave_balances(self):
 return self.data_source.get_leave_balances(self.employee_id)

 def get_leave_history(self):
 return self.data_source.get_leave_history(self.employee_id)

 def display_dashboard(self):
 profile = self.get_profile()
 balances = self.get_leave_balances()
 history = self.get_leave_history()
 print(f"Profile: {profile}")
 print(f"Leave Balances: {balances}")
 print("Leave History:")
 for leave in history:
 print(leave)

# Example usage (assuming data_source implements required methods):
# dashboard = EmployeeDashboard('emp001', data_source)
# dashboard.display_dashboard()
