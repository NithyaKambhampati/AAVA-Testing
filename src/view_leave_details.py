class LeaveDetails:
    def __init__(self, employee_id, db):
        self.employee_id = employee_id
        self.db = db

    def get_personal_info(self):
        return self.db.get_employee(self.employee_id)

    def get_leave_balances(self):
        return self.db.get_leave_balances(self.employee_id)

    def get_leave_history(self):
        return self.db.get_leave_history(self.employee_id)

    def display(self):
        info = self.get_personal_info()
        balances = self.get_leave_balances()
        history = self.get_leave_history()
        print(f"Employee: {info['name']} ({info['email']})")
        print("Leave Balances:")
        for leave_type, balance in balances.items():
            print(f"  {leave_type}: {balance}")
        print("Leave History:")
        for req in history:
            print(f"  {req['leave_type']} from {req['start_date']} to {req['end_date']} - {req['status']}")

# Example usage:
if __name__ == "__main__":
    class DummyDB:
        def get_employee(self, eid):
            return {'name': 'Alice', 'email': 'alice@org.com'}
        def get_leave_balances(self, eid):
            return {'casual': 5, 'sick': 2, 'earned': 10}
        def get_leave_history(self, eid):
            return [
                {'leave_type': 'casual', 'start_date': '2024-06-01', 'end_date': '2024-06-03', 'status': 'approved'},
                {'leave_type': 'sick', 'start_date': '2024-05-10', 'end_date': '2024-05-10', 'status': 'rejected'}
            ]
    db = DummyDB()
    ld = LeaveDetails(employee_id=1, db=db)
    ld.display()