"""
HR/Admin Leave Configuration and Policy Management
As an HR/Admin, I want to configure leave types, policies, accrual rules, and holiday calendars so that the system reflects organizational policies.
"""

class HRPolicyService:
    def __init__(self, policy_repo):
        self.policy_repo = policy_repo

    def add_leave_type(self, name: str, accrual_policy: dict):
        self.policy_repo.create_leave_type(name, accrual_policy)

    def update_policy(self, policy_id: int, config: dict):
        self.policy_repo.update_policy(policy_id, config)

    def set_holiday_calendar(self, holidays: list):
        self.policy_repo.set_holiday_calendar(holidays)
