class LeaveValidator:
    def __init__(self, db):
        self.db = db

    def validate(self, employee_id, leave_type, start_date, end_date):
        balance = self.db.get_leave_balance(employee_id, leave_type)
        days = self.db.calculate_days(start_date, end_date)
        if balance < days:
            return {'status': 'error', 'message': 'Insufficient leave balance'}
        if self.db.is_overlapping(employee_id, start_date, end_date):
            return {'status': 'error', 'message': 'Overlapping dates'}
        if not self.db.is_valid_date_range(start_date, end_date):
            return {'status': 'error', 'message': 'Invalid date selection'}
        return {'status': 'success', 'message': 'Leave request is valid'}

# Example usage:
if __name__ == "__main__":
    class DummyDB:
        def get_leave_balance(self, eid, leave_type):
            return 5
        def calculate_days(self, start, end):
            from datetime import datetime
            s = datetime.strptime(start, '%Y-%m-%d')
            e = datetime.strptime(end, '%Y-%m-%d')
            return (e - s).days + 1
        def is_overlapping(self, eid, start, end):
            return False
        def is_valid_date_range(self, start, end):
            from datetime import datetime
            s = datetime.strptime(start, '%Y-%m-%d')
            e = datetime.strptime(end, '%Y-%m-%d')
            return s <= e
    db = DummyDB()
    validator = LeaveValidator(db)
    result = validator.validate(1, 'casual', '2024-06-10', '2024-06-12')
    print(result)