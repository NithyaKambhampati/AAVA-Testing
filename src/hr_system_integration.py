"""
System Integration with HR/Employee Systems
As the system, I want to integrate with existing employee and HR systems, so that data is consistent and workflows are seamless.
"""
class HRIntegration:
    def __init__(self, hr_system):
        self.hr_system = hr_system

    def sync_employee_data(self, employee_id):
        # Simulate HR system sync (stub)
        if employee_id in self.hr_system:
            return {'status': 'success', 'data': self.hr_system[employee_id]}
        else:
            return {'status': 'error', 'message': 'Employee not found in HR system'}

    def update_leave_policy(self, policy):
        # Simulate updating policy in HR system
        self.hr_system['policies'].append(policy)
        return {'status': 'success', 'message': 'Policy updated'}

# Example usage
if __name__ == '__main__':
    hr_system = {
        'E123': {'name': 'John Doe', 'role': 'employee'},
        'policies': []
    }
    integration = HRIntegration(hr_system)
    print(integration.sync_employee_data('E123'))
    print(integration.update_leave_policy({'type': 'casual', 'max_days': 12}))
