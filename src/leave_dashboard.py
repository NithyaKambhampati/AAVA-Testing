"""
View Personal Leave Dashboard
As an employee, I want to view my personal details, leave balances, and leave history so that I can track my leave status and plan accordingly.
"""

class LeaveDashboard:
    def __init__(self, user_service, leave_service):
        self.user_service = user_service
        self.leave_service = leave_service

    def get_dashboard(self, user_id: int) -> dict:
        user_details = self.user_service.get_user_details(user_id)
        leave_balances = self.leave_service.get_leave_balances(user_id)
        leave_history = self.leave_service.get_leave_history(user_id)
        return {
            'user_details': user_details,
            'leave_balances': leave_balances,
            'leave_history': leave_history
        }
