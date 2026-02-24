class LeaveApplication:
    def __init__(self, employee_id, db):
        self.employee_id = employee_id
        self.db = db

    def apply_leave(self, leave_type, start_date, end_date, reason=None):
        if leave_type not in self.db.get_configured_leave_types():
            return {'status': 'error', 'message': 'Invalid leave type'}
        if not self.db.has_sufficient_balance(self.employee_id, leave_type, start_date, end_date):
            return {'status': 'error', 'message': 'Insufficient leave balance'}
        if self.db.is_overlapping(self.employee_id, start_date, end_date):
            return {'status': 'error', 'message': 'Overlapping leave dates'}
        request_id = self.db.create_leave_request(self.employee_id, leave_type, start_date, end_date, reason)
        return {'status': 'success', 'message': 'Leave request submitted', 'request_id': request_id}

# Example usage:
if __name__ == "__main__":
    class DummyDB:
        def get_configured_leave_types(self):
            return ['casual', 'sick', 'earned']
        def has_sufficient_balance(self, eid, leave_type, start_date, end_date):
            return True
        def is_overlapping(self, eid, start_date, end_date):
            return False
        def create_leave_request(self, eid, leave_type, start_date, end_date, reason):
            return 123
    db = DummyDB()
    la = LeaveApplication(employee_id=1, db=db)
    result = la.apply_leave('casual', '2024-06-10', '2024-06-12', 'Vacation')
    print(result)