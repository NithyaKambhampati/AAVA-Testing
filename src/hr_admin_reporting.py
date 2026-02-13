"""
HR/Admin Reporting and Analytics
As an HR/admin user, I want to view leave reports and analytics across teams and the organization, so that I can monitor leave trends and compliance.
"""
class LeaveReporting:
    def __init__(self, leave_requests):
        self.leave_requests = leave_requests

    def aggregate_leave_data(self):
        summary = {}
        for req in self.leave_requests:
            typ = req['type']
            summary.setdefault(typ, {'total': 0, 'approved': 0, 'pending': 0, 'rejected': 0})
            summary[typ]['total'] += 1
            summary[typ][req['status']] += 1
        return summary

    def pending_approvals(self):
        return [req for req in self.leave_requests if req['status'] == 'pending']

# Example usage
if __name__ == '__main__':
    leave_requests = [
        {'employee_id': 'E123', 'type': 'casual', 'start': '2024-07-01', 'end': '2024-07-02', 'status': 'approved'},
        {'employee_id': 'E124', 'type': 'sick', 'start': '2024-07-03', 'end': '2024-07-03', 'status': 'pending'},
        {'employee_id': 'E125', 'type': 'earned', 'start': '2024-07-05', 'end': '2024-07-06', 'status': 'rejected'}
    ]
    reporting = LeaveReporting(leave_requests)
    print(reporting.aggregate_leave_data())
    print(reporting.pending_approvals())
