"""
HR/Admin Leave Policy Configuration Module
- Allows HR/Admin to configure leave types, policies, accrual rules, and holiday calendars
- Prevents duplicate leave types
"""

class PolicyConfigurationError(Exception):
    pass

class LeavePolicyConfigService:
    def __init__(self, admin_client):
        self.admin_client = admin_client

    def add_leave_type(self, leave_type: str, accrual_rule: dict) -> bool:
        existing_types = self.admin_client.fetch_leave_types()
        if leave_type in existing_types:
            raise PolicyConfigurationError("Duplicate leave type detected.")
        try:
            self.admin_client.create_leave_type(leave_type, accrual_rule)
            return True
        except Exception as e:
            raise PolicyConfigurationError(f"Failed to add leave type: {str(e)}")

    def configure_policy(self, policy_data: dict) -> bool:
        try:
            self.admin_client.update_policy(policy_data)
            return True
        except Exception as e:
            raise PolicyConfigurationError(f"Policy configuration failed: {str(e)}")

    def set_holiday_calendar(self, holidays: list) -> bool:
        try:
            self.admin_client.update_holiday_calendar(holidays)
            return True
        except Exception as e:
            raise PolicyConfigurationError(f"Holiday calendar update failed: {str(e)}")
