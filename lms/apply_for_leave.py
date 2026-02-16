"""
Apply for Leave Module
- Handles leave application creation and validation
- Validates balance, date ranges, and overlapping requests
"""

from datetime import datetime
from typing import Optional, List, Dict

class LeaveApplicationError(Exception):
    pass

class LeaveApplicationService:
    def __init__(self, hr_client, holiday_calendar):
        self.hr_client = hr_client
        self.holiday_calendar = holiday_calendar

    def is_valid_dates(self, start_date: str, end_date: str) -> bool:
        try:
            sd = datetime.strptime(start_date, '%Y-%m-%d')
            ed = datetime.strptime(end_date, '%Y-%m-%d')
            return sd <= ed
        except Exception:
            return False

    def is_nonworking_day(self, date: str) -> bool:
        return date in self.holiday_calendar

    def has_overlapping_leave(self, employee_id: str, start_date: str, end_date: str) -> bool:
        history = self.hr_client.fetch_leave_history(employee_id)
        for leave in history:
            if leave['status'] in ('APPROVED','REQUESTED'):
                if not (end_date < leave['start_date'] or start_date > leave['end_date']):
                    return True
        return False

    def apply_leave(self, employee_id: str, leave_type: str, start_date: str, end_date: str, reason: Optional[str]=None) -> Dict:
        if not self.is_valid_dates(start_date, end_date):
            raise LeaveApplicationError("Start date must be before or equal to end date.")
        if self.has_overlapping_leave(employee_id, start_date, end_date):
            raise LeaveApplicationError("Overlapping leave request detected.")
        for date in [start_date, end_date]:
            if self.is_nonworking_day(date):
                raise LeaveApplicationError(f"{date} is a non-working day.")
        balances = self.hr_client.fetch_leave_balances(employee_id)
        days_requested = (datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days + 1
        if balances.get(leave_type, 0) < days_requested:
            raise LeaveApplicationError("Insufficient leave balance.")
        # All validations passed, create leave request
        leave_request = {
            'employee_id': employee_id,
            'leave_type': leave_type,
            'start_date': start_date,
            'end_date': end_date,
            'reason': reason,
            'status': 'REQUESTED'
        }
        self.hr_client.create_leave_request(leave_request)
        return leave_request
