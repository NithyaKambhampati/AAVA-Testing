# leave_balance.py

from typing import Dict
from datetime import datetime

class LeaveBalanceManager:
    def __init__(self, leave_balances: Dict[str, int]):
        self.leave_balances = leave_balances
        self.audit_log = []

    def update_balance_on_approval(self, leave_type: str, days: int, user_id: str):
        if leave_type in self.leave_balances:
            self.leave_balances[leave_type] -= days
            self._log_action(user_id, 'balance_update', leave_type, days)
            return {"message": "Balance updated", "leave_balances": self.leave_balances}
        return {"error": "Leave type not found"}

    def no_update_on_rejection_or_cancellation(self, user_id: str, leave_type: str):
        self._log_action(user_id, 'no_balance_change', leave_type, 0)
        return {"message": "Balance unchanged", "leave_balances": self.leave_balances}

    def manual_override(self, leave_type: str, new_balance: int, admin_id: str):
        self.leave_balances[leave_type] = new_balance
        self._log_action(admin_id, 'manual_override', leave_type, new_balance)
        return {"message": "Manual override complete", "leave_balances": self.leave_balances}

    def _log_action(self, user_id: str, action: str, leave_type: str, value: int):
        self.audit_log.append({
            "user_id": user_id,
            "action": action,
            "leave_type": leave_type,
            "value": value,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_audit_log(self):
        return self.audit_log

# Example usage
if __name__ == "__main__":
    balances = {'sick': 5, 'casual': 7}
    manager = LeaveBalanceManager(balances)
    print(manager.update_balance_on_approval('casual', 2, 'emp001'))
    print(manager.no_update_on_rejection_or_cancellation('emp001', 'casual'))
    print(manager.manual_override('sick', 10, 'admin001'))
    print(manager.get_audit_log())
