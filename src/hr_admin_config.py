"""
HR/Admin Configuration of Leave Types and Policies
As an HR/admin user, I want to configure leave types, policies, accrual rules, and holiday calendars, so that leave management aligns with organizational policies.
"""
class LeaveConfig:
    def __init__(self):
        self.leave_types = {}
        self.accrual_rules = {}
        self.holiday_calendar = set()

    def add_leave_type(self, name, max_days, accrual_rule):
        self.leave_types[name] = {'max_days': max_days, 'accrual_rule': accrual_rule}

    def set_accrual_rule(self, name, rule):
        self.accrual_rules[name] = rule

    def add_holiday(self, date_str, description):
        self.holiday_calendar.add((date_str, description))

    def remove_holiday(self, date_str):
        self.holiday_calendar = set([h for h in self.holiday_calendar if h[0] != date_str])

# Example usage
if __name__ == '__main__':
    config = LeaveConfig()
    config.add_leave_type('casual', 12, 'monthly')
    config.set_accrual_rule('casual', '1 day per month')
    config.add_holiday('2024-12-25', 'Christmas Day')
    print(config.leave_types)
    print(config.accrual_rules)
    print(config.holiday_calendar)
