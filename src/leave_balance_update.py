# leave_balance_update.py
"""
Automatic Leave Balance Update on Approval
Updates employee leave balances after approval, ensures rejected/cancelled requests do not affect balances.
"""
from typing import Dict

class LeaveBalanceManager:
    def __init__(self, balances: Dict[str, int]):
        self.balances = balances

    def update_balance(self, leave_type: str, days: int, action: str):
        if action == "approved":
            if self.balances.get(leave_type, 0) >= days:
                self.balances[leave_type] -= days
                print(f"{days} days deducted from {leave_type}. New balance: {self.balances[leave_type]}")
            else:
                print("Insufficient balance to deduct.")
        elif action in ("rejected", "cancelled"):
            print("No balance change for rejected/cancelled requests.")
        else:
            print("Unknown action.")

if __name__ == "__main__":
    balances = {"Casual": 5, "Sick": 8, "Earned": 12}
    manager = LeaveBalanceManager(balances)
    manager.update_balance("Casual", 2, "approved")
    manager.update_balance("Sick", 2, "rejected")
    manager.update_balance("Earned", 1, "cancelled")
