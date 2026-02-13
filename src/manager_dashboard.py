"""
Manager Dashboard for Leave Requests
As a manager, I want to view all pending leave requests from my team in a dashboard, so that I can manage approvals efficiently.
"""
class ManagerDashboard:
    def __init__(self, manager_id, leave_requests):
        self.manager_id = manager_id
        self.leave_requests = leave_requests

    def get_pending_requests(self):
        pending = [req for req in self.leave_requests if req['manager_id'] == self.manager_id and req['status'] == 'pending']
        return pending

# Example usage
if __name__ == '__main__':
    leave_requests = [
        {'employee_id': 'E123', 'manager_id': 'M456', 'type': 'casual', 'start': '2024-07-01', 'end': '2024-07-02', 'status': 'pending', 'reason': 'Vacation'},
        {'employee_id': 'E124', 'manager_id': 'M456', 'type': 'sick', 'start': '2024-07-03', 'end': '2024-07-03', 'status': 'approved', 'reason': 'Flu'},
        {'employee_id': 'E125', 'manager_id': 'M789', 'type': 'earned', 'start': '2024-07-05', 'end': '2024-07-06', 'status': 'pending', 'reason': 'Personal'}
    ]
    dashboard = ManagerDashboard('M456', leave_requests)
    print(dashboard.get_pending_requests())
