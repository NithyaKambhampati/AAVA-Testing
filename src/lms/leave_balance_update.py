"""
Automatic Leave Balance Update
User Story: As the LMS, I want to update leave balances only upon approval and not for cancelled or rejected requests so that records remain accurate.
Acceptance Criteria:
- Approved: balance reduced.
- Rejected/cancelled before approval: balance unchanged.
"""

from typing import Dict

class LeaveBalanceService:
    def __init__(self, balances: Dict[str, Dict[str, int]]):
        self.balances = balances  # employee_id -> {leave_type: balance}

    def update_balance(self, employee_id: str, leave_type: str, days: int, status: str) -> str:
        if status == "approved":
            if self.balances[employee_id][leave_type] < days:
                return "Error: Insufficient balance."
            self.balances[employee_id][leave_type] -= days
            return f"Balance updated. New {leave_type} balance: {self.balances[employee_id][leave_type]}"
        elif status in ["rejected", "cancelled"]:
            return "Leave balance unchanged."
        else:
            return "No action taken."

# Example usage:
if __name__ == "__main__":
    balances = {"E123": {"casual": 5, "sick": 8}}
    svc = LeaveBalanceService(balances)
    print(svc.update_balance("E123", "casual", 2, "approved"))
    print(svc.update_balance("E123", "casual", 2, "rejected"))
    print(svc.update_balance("E123", "casual", 2, "pending"))
