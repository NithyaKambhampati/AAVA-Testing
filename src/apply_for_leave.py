"""
Apply for Leave
As an employee, I want to apply for different leave types, so that my leave requests are processed according to organizational policy.
"""
from datetime import datetime

class LeaveApplication:
    def __init__(self, employee, leave_type, start_date, end_date, reason=None):
        self.employee = employee
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.status = 'pending'

    def validate(self):
        # Check sufficient balance
        days = (self.end_date - self.start_date).days + 1
        if self.leave_type not in self.employee.leave_balances:
            return False, 'Invalid leave type'
        if self.employee.leave_balances[self.leave_type] < days:
            return False, 'Insufficient leave balance'
        # Check for overlapping dates
        for leave in self.employee.leave_history:
            if leave['status'] in ['approved', 'pending']:
                existing_start = datetime.strptime(leave['start'], '%Y-%m-%d')
                existing_end = datetime.strptime(leave['end'], '%Y-%m-%d')
                if not (self.end_date < existing_start or self.start_date > existing_end):
                    return False, 'Leave dates overlap with existing request'
        return True, 'Valid leave request'

    def submit(self):
        valid, msg = self.validate()
        if valid:
            self.status = 'pending'
            # Route to manager (simulated)
            return {'status': 'success', 'message': 'Leave request submitted and routed to manager.'}
        else:
            return {'status': 'error', 'message': msg}

# Example usage
if __name__ == '__main__':
    from view_personal_details import Employee
    leave_balances = {'casual': 8, 'sick': 5, 'earned': 12}
    leave_history = [
        {'type': 'casual', 'start': '2024-05-01', 'end': '2024-05-02', 'status': 'approved'},
        {'type': 'sick', 'start': '2024-06-10', 'end': '2024-06-11', 'status': 'rejected'}
    ]
    emp = Employee('E123', 'John Doe', leave_balances, leave_history)
    app = LeaveApplication(emp, 'casual', datetime(2024, 7, 1), datetime(2024, 7, 2), 'Vacation')
    print(app.submit())
