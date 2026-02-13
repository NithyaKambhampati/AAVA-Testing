"""
HR/Admin: Configure Leave Types, Policies, and Calendars
Allows HR/Admin to configure leave types, policies, accrual rules, and holiday calendars. Creates audit log entries for changes.
"""

from typing import Dict, List
from datetime import datetime

class LeaveTypeConfig:
    def __init__(self, name: str, accrual_rule: str, active: bool = True):
        self.name = name
        self.accrual_rule = accrual_rule
        self.active = active

class PolicyConfig:
    def __init__(self, name: str, description: str, rules: Dict):
        self.name = name
        self.description = description
        self.rules = rules
        self.effective_date = datetime.now().strftime("%Y-%m-%d")

class HolidayCalendar:
    def __init__(self):
        self.holidays = []  # List of (date, description)
    def add_holiday(self, date: str, description: str):
        self.holidays.append((date, description))

class AuditLog:
    def __init__(self):
        self.entries = []
    def log(self, user_id: str, action: str, target: str, details: str):
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_id": user_id,
            "action": action,
            "target": target,
            "details": details
        }
        self.entries.append(entry)
        print(f"Audit log: {entry}")

class HRConfig:
    def __init__(self, user_id: str, audit_log: AuditLog):
        self.leave_types: Dict[str, LeaveTypeConfig] = {}
        self.policies: Dict[str, PolicyConfig] = {}
        self.holiday_calendar = HolidayCalendar()
        self.user_id = user_id
        self.audit_log = audit_log
    def add_leave_type(self, name: str, accrual_rule: str):
        self.leave_types[name] = LeaveTypeConfig(name, accrual_rule)
        self.audit_log.log(self.user_id, "Add Leave Type", name, f"Accrual: {accrual_rule}")
    def add_policy(self, name: str, description: str, rules: Dict):
        self.policies[name] = PolicyConfig(name, description, rules)
        self.audit_log.log(self.user_id, "Add Policy", name, description)
    def add_holiday(self, date: str, description: str):
        self.holiday_calendar.add_holiday(date, description)
        self.audit_log.log(self.user_id, "Add Holiday", date, description)

# Example usage
if __name__ == "__main__":
    audit_log = AuditLog()
    hr = HRConfig("hr_admin", audit_log)
    hr.add_leave_type("casual", "1 per month")
    hr.add_policy("max_consecutive", "Max 10 days at a time", {"max_days": 10})
    hr.add_holiday("2024-12-25", "Christmas")
