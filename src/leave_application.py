# leave_application.py
"""
Employee Leave Application Submission
Allows employees to apply for leave, with validation for balance, overlap, and policy.
"""
from typing import List, Dict
from datetime import datetime

class LeaveApplicationError(Exception):
    pass

class LeavePolicy:
    def __init__(self, min_notice_days: int = 0, max_days_per_request: int = 30):
        self.min_notice_days = min_notice_days
        self.max_days_per_request = max_days_per_request

class LeaveManager:
    def __init__(self, leave_balances: Dict[str, int], leave_history: List[Dict], policy: LeavePolicy):
        self.leave_balances = leave_balances
        self.leave_history = leave_history
        self.policy = policy

    def is_overlapping(self, start_date: str, end_date: str) -> bool:
        s = datetime.strptime(start_date, "%Y-%m-%d")
        e = datetime.strptime(end_date, "%Y-%m-%d")
        for record in self.leave_history:
            rs = datetime.strptime(record["start_date"], "%Y-%m-%d")
            re = datetime.strptime(record["end_date"], "%Y-%m-%d")
            if (s <= re and e >= rs) and record["status"] in ("Pending", "Approved"):
                return True
        return False

    def apply_leave(self, leave_type: str, start_date: str, end_date: str, reason: str = "") -> str:
        if leave_type not in self.leave_balances:
            raise LeaveApplicationError("Invalid leave type")
        s = datetime.strptime(start_date, "%Y-%m-%d")
        e = datetime.strptime(end_date, "%Y-%m-%d")
        if e < s:
            raise LeaveApplicationError("End date cannot be before start date")
        days_requested = (e - s).days + 1
        if days_requested > self.leave_balances[leave_type]:
            raise LeaveApplicationError("Insufficient leave balance")
        if self.is_overlapping(start_date, end_date):
            raise LeaveApplicationError("Overlapping leave request detected")
        today = datetime.today()
        if (s - today).days < self.policy.min_notice_days:
            raise LeaveApplicationError(f"Must apply at least {self.policy.min_notice_days} days in advance")
        if days_requested > self.policy.max_days_per_request:
            raise LeaveApplicationError(f"Cannot request more than {self.policy.max_days_per_request} days at once")
        # Simulate submission
        self.leave_history.append({
            "leave_type": leave_type,
            "start_date": start_date,
            "end_date": end_date,
            "status": "Pending",
            "reason": reason
        })
        return "Leave request submitted for approval"

if __name__ == "__main__":
    balances = {"Casual": 5, "Sick": 8, "Earned": 12}
    history = []
    policy = LeavePolicy(min_notice_days=1, max_days_per_request=15)
    manager = LeaveManager(balances, history, policy)
    try:
        msg = manager.apply_leave(
            leave_type=input("Leave type: "),
            start_date=input("Start date (YYYY-MM-DD): "),
            end_date=input("End date (YYYY-MM-DD): "),
            reason=input("Reason (optional): ")
        )
        print(msg)
    except LeaveApplicationError as e:
        print(f"Error: {e}")
