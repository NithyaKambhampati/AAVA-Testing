"""
Automatic Leave Balance Adjustment
As an employee, I want my leave balance to update only after approval, so that my records are always accurate.
"""

class LeaveBalanceService:
    def __init__(self, balance_repo):
        self.balance_repo = balance_repo

    def update_balance_on_approval(self, user_id: int, leave_type: str, days: int):
        self.balance_repo.decrement_balance(user_id, leave_type, days)

    def no_change_on_reject_or_cancel(self):
        pass # No action needed for rejected or cancelled requests
