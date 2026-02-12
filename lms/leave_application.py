# lms/leave_application.py
"""
Handles leave application logic, validation, and routing to managers.
"""
from datetime import date
from typing import List, Dict

class LeaveValidationError(Exception):
 pass

def validate_leave_application(employee, leave_type: str, start_date: date, end_date: date, reason: str, existing_requests: List[Dict]) -> bool:
 """
 Validates leave application for sufficient balance and date conflicts.
 """
 if leave_type not in employee.leave_balances:
 raise LeaveValidationError("Leave type not configured.")
 if (end_date < start_date):
 raise LeaveValidationError("Invalid date range.")
 days_requested = (end_date - start_date).days + 1
 if employee.leave_balances[leave_type] < days_requested:
 raise LeaveValidationError("Insufficient leave balance.")
 for req in existing_requests:
 if req['status'] in ['Pending', 'Approved']:
 if not (end_date < req['start_date'] or start_date > req['end_date']):
 raise LeaveValidationError("Overlapping leave dates.")
 if start_date < date.today():
 raise LeaveValidationError("Cannot apply for leave in the past.")
 return True

def submit_leave_request(employee, leave_type: str, start_date: date, end_date: date, reason: str, existing_requests: List[Dict]):
 if validate_leave_application(employee, leave_type, start_date, end_date, reason, existing_requests):
 request = {
 'leave_type': leave_type,
 'start_date': start_date,
 'end_date': end_date,
 'reason': reason,
 'status': 'Pending',
 }
 employee.add_leave_request(request)
 return request
