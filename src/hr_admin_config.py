# hr_admin_config.py

from typing import Dict, List
from datetime import datetime

class HRAdminConfig:
    def __init__(self):
        self.leave_types = {}
        self.policies = {}
        self.holiday_calendar = []
        self.audit_log = []

    def add_leave_type(self, leave_type: str, accrual_rule: str):
        self.leave_types[leave_type] = accrual_rule
        self._log_action('add_leave_type', leave_type, accrual_rule)

    def set_policy(self, leave_type: str, policy: str):
        self.policies[leave_type] = policy
        self._log_action('set_policy', leave_type, policy)

    def add_holiday(self, date: str, description: str):
        self.holiday_calendar.append({"date": date, "description": description})
        self._log_action('add_holiday', date, description)

    def update_holiday(self, date: str, new_description: str):
        for holiday in self.holiday_calendar:
            if holiday['date'] == date:
                holiday['description'] = new_description
                self._log_action('update_holiday', date, new_description)

    def _log_action(self, action: str, key: str, value: str):
        self.audit_log.append({
            "action": action,
            "key": key,
            "value": value,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_audit_log(self):
        return self.audit_log

# Example usage
if __name__ == "__main__":
    config = HRAdminConfig()
    config.add_leave_type('casual', 'accrue_monthly')
    config.set_policy('casual', 'max 7 days/year')
    config.add_holiday('2024-06-15', 'Company Anniversary')
    config.update_holiday('2024-06-15', 'Annual Day')
    print(config.leave_types)
    print(config.policies)
    print(config.holiday_calendar)
    print(config.get_audit_log())
