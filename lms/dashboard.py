# lms/dashboard.py
"""
Employee dashboard and leave history management.
"""

from typing import List, Dict

class Employee:
 def __init__(self, emp_id: str, name: str, leave_balances: Dict[str, int]):
 self.emp_id = emp_id
 self.name = name
 self.leave_balances = leave_balances
 self.leave_history = [] # List of leave requests

 def view_dashboard(self) -> Dict:
 return {
 'id': self.emp_id,
 'name': self.name,
 'leave_balances': self.leave_balances,
 'leave_history': self.leave_history if self.leave_history else 'No history'
 }

 def add_leave_request(self, request: Dict):
 self.leave_history.append(request)
