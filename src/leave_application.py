# leave_application.py

from datetime import datetime
from typing import List, Dict

class LeaveApplication:
    def __init__(self, leave_balances: Dict[str, int], holidays: List[str], leave_history: List[Dict]):
        self.leave_balances = leave_balances
        self.holidays = holidays  # List of holiday dates as strings
        self.leave_history = leave_history
        self.audit_log = []

    def apply_leave(self, leave_type: str, start_date: str, end_date: str, comments: str = "") -> Dict:
        # Validate leave type
        if leave_type not in self.leave_balances:
            return {"error": "Invalid leave type"}
        # Validate date format
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return {"error": "Invalid date format"}
        # Validate date logic
        if end < start:
            return {"error": "End date cannot be before start date"}
        # Validate overlaps
        for req in self.leave_history:
            if req['status'] == 'approved':
                req_start = datetime.strptime(req['start'], "%Y-%m-%d")
                req_end = datetime.strptime(req['end'], "%Y-%m-%d")
                if (start <= req_end and end >= req_start):
                    return {"error": "Dates overlap with existing approved leave"}
        # Validate holidays
        for day in self._daterange(start, end):
            if day.strftime("%Y-%m-%d") in self.holidays:
                return {"error": "Leave request spans a holiday"}
        # Validate sufficient balance
        days = (end - start).days + 1
        if self.leave_balances[leave_type] < days:
            return {"error": "Insufficient leave balance"}
        # Create leave request
        request = {
            "type": leave_type,
            "start": start_date,
            "end": end_date,
            "status": "pending",
            "comments": comments
        }
        self.leave_history.append(request)
        self._log_action("apply_leave", request)
        return {"message": "Leave request submitted", "request": request}

    def _daterange(self, start, end):
        for n in range(int((end - start).days) + 1):
            yield start + timedelta(days=n)

    def _log_action(self, action: str, data: Dict):
        self.audit_log.append({
            "action": action,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_audit_log(self):
        return self.audit_log

# Example usage
if __name__ == "__main__":
    from datetime import timedelta
    balances = {'sick': 5, 'casual': 7}
    holidays = ['2024-06-15']
    history = [
        {"type": "sick", "start": "2024-06-01", "end": "2024-06-03", "status": "approved"}
    ]
    leave_app = LeaveApplication(balances, holidays, history)
    print(leave_app.apply_leave('casual', '2024-06-10', '2024-06-12', 'Vacation'))
    print(leave_app.apply_leave('casual', '2024-06-15', '2024-06-16', 'Holiday overlap'))
    print(leave_app.get_audit_log())
