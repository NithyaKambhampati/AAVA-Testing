# US-101: Apply for Leave
"""
Module: test2.py
Implements the 'Apply for Leave' user story for employees.
"""
import datetime

class LeaveApplication:
    def __init__(self, employee_id, leave_balance):
        """
        Initialize LeaveApplication with employee ID and leave balance.
        :param employee_id: str
        :param leave_balance: int (number of days)
        """
        self.employee_id = employee_id
        self.leave_balance = leave_balance
        self.leave_requests = []  # Store leave requests

    def apply_leave(self, start_date_str, end_date_str):
        """
        Apply for leave by providing start and end dates.
        :param start_date_str: str (YYYY-MM-DD)
        :param end_date_str: str (YYYY-MM-DD)
        :return: dict (confirmation or error)
        """
        try:
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            return {"success": False, "message": "Invalid date format. Use YYYY-MM-DD."}

        # Check for past dates
        today = datetime.date.today()
        if start_date < today or end_date < today:
            return {"success": False, "message": "Past dates are not allowed."}

        # Check that end date is after start date
        if end_date < start_date:
            return {"success": False, "message": "End date must be after start date."}

        # Calculate leave days
        leave_days = (end_date - start_date).days + 1
        if leave_days <= 0:
            return {"success": False, "message": "Leave duration must be at least 1 day."}

        # Validate leave balance
        if leave_days > self.leave_balance:
            return {"success": False, "message": "Insufficient leave balance."}

        # Store leave request
        leave_request = {
            "employee_id": self.employee_id,
            "start_date": start_date_str,
            "end_date": end_date_str,
            "leave_days": leave_days,
            "status": "Submitted"
        }
        self.leave_requests.append(leave_request)
        self.leave_balance -= leave_days

        # Confirmation
        return {
            "success": True,
            "message": f"Leave request submitted successfully for {leave_days} days.",
            "request": leave_request
        }

    def get_leave_requests(self):
        """
        Retrieve all leave requests for this employee.
        :return: list
        """
        return self.leave_requests

# Example usage and test cases
if __name__ == "__main__":
    # Initialize with 10 leave days
    app = LeaveApplication(employee_id="E123", leave_balance=10)

    # Valid leave request
    result = app.apply_leave(
        start_date_str=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
        end_date_str=(datetime.date.today() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
    )
    print(result)

    # Invalid date format
    result = app.apply_leave("2024/06/01", "2024/06/05")
    print(result)

    # Past date
    result = app.apply_leave("2020-01-01", "2020-01-05")
    print(result)

    # Insufficient leave balance
    result = app.apply_leave(
        start_date_str=(datetime.date.today() + datetime.timedelta(days=4)).strftime("%Y-%m-%d"),
        end_date_str=(datetime.date.today() + datetime.timedelta(days=15)).strftime("%Y-%m-%d")
    )
    print(result)

    # End date before start date
    result = app.apply_leave(
        start_date_str=(datetime.date.today() + datetime.timedelta(days=5)).strftime("%Y-%m-%d"),
        end_date_str=(datetime.date.today() + datetime.timedelta(days=2)).strftime("%Y-%m-%d")
    )
    print(result)

    # Check stored requests
    print("All leave requests:", app.get_leave_requests())
