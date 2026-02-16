"""
Validation of Leave Requests
User Story: As the LMS, I want to validate leave applications for balance, overlapping, and date correctness so that only eligible requests are processed.
Acceptance Criteria:
- Insufficient balance, overlapping requests, or invalid dates are rejected with explanatory message.
"""

from datetime import date
from typing import List, Dict

class LeaveValidator:
    def __init__(self, balances: Dict[str, Dict[str, int]], requests: List[Dict]):
        self.balances = balances  # employee_id -> {leave_type: balance}
        self.requests = requests  # List of leave dicts

    def validate(self, employee_id: str, leave_type: str, start_date: date, end_date: date, days: int) -> str:
        if end_date < start_date:
            return "Error: Invalid date range."
        if self.balances[employee_id][leave_type] < days:
            return "Error: Insufficient leave balance."
        for req in self.requests:
            if req["employee_id"] == employee_id and req["status"] in ["pending", "approved"]:
                if not (end_date < req["start_date"] or start_date > req["end_date"]):
                    return "Error: Overlapping leave request."
        return "Validation successful."

# Example usage:
if __name__ == "__main__":
    balances = {"E123": {"casual": 5, "sick": 8}}
    requests = [
        {"employee_id": "E123", "leave_type": "casual", "start_date": date(2024,6,10), "end_date": date(2024,6,12), "status": "approved"}
    ]
    validator = LeaveValidator(balances, requests)
    print(validator.validate("E123", "casual", date(2024,6,11), date(2024,6,13), 3))  # Overlap
    print(validator.validate("E123", "casual", date(2024,6,15), date(2024,6,14), 0))  # Invalid date
    print(validator.validate("E123", "casual", date(2024,6,20), date(2024,6,30), 11))  # Insufficient balance
    print(validator.validate("E123", "casual", date(2024,6,13), date(2024,6,13), 1))  # Success
