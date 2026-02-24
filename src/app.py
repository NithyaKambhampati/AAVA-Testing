def apply_leave(self, leave_type, start_date, end_date, reason=None):
        if leave_type not in self.db.get_configured_leave_types():
            return {'status': 'error', 'message': 'Invalid leave type'}
        if not self.db.has_sufficient_balance(self.employee_id, leave_type, start_date, end_date):
            return {'status': 'error', 'message': 'Insufficient leave balance'}
        if self.db.is_overlapping(self.employee_id, start_date, end_date):
            return {'status': 'error', 'message': 'Overlapping leave dates'}
        request_id = self.db.create_leave_request(self.employee_id, leave_type, start_date, end_date, reason)
        return {'status': 'success', 'message': 'Leave request submitted', 'request_id': request_id}