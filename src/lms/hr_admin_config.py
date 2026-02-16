"""
HR/Admin Configuration of Leave Types and Policies
User Story: As an HR/admin, I want to configure leave types, accrual rules, and holiday calendars so that the LMS aligns with organizational policies.
Acceptance Criteria:
- HR/admin can add/modify leave types or policies; employees can apply as per updated configurations.
"""

from typing import Dict, List

class LeaveType:
    def __init__(self, name: str, accrual_rule: str, max_days: int):
        self.name = name
        self.accrual_rule = accrual_rule
        self.max_days = max_days

class HRAdminConfigService:
    def __init__(self):
        self.leave_types: Dict[str, LeaveType] = {}
        self.holidays: List[str] = []

    def add_leave_type(self, name: str, accrual_rule: str, max_days: int) -> str:
        if name in self.leave_types:
            return f"Leave type '{name}' already exists."
        self.leave_types[name] = LeaveType(name, accrual_rule, max_days)
        return f"Leave type '{name}' added."

    def modify_leave_type(self, name: str, accrual_rule: str = None, max_days: int = None) -> str:
        if name not in self.leave_types:
            return f"Leave type '{name}' not found."
        if accrual_rule:
            self.leave_types[name].accrual_rule = accrual_rule
        if max_days is not None:
            self.leave_types[name].max_days = max_days
        return f"Leave type '{name}' updated."

    def add_holiday(self, date_str: str) -> str:
        if date_str in self.holidays:
            return f"Holiday '{date_str}' already exists."
        self.holidays.append(date_str)
        return f"Holiday '{date_str}' added."

# Example usage:
if __name__ == "__main__":
    svc = HRAdminConfigService()
    print(svc.add_leave_type("casual", "monthly", 12))
    print(svc.modify_leave_type("casual", max_days=15))
    print(svc.add_holiday("2024-12-25"))
