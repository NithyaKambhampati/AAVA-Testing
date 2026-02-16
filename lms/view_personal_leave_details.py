"""
View Personal Leave Details Module
- Displays employee info, leave balances, and leave history
- Real-time sync with HR system
"""

from typing import List, Dict

class LeaveDataSyncError(Exception):
    pass

class EmployeeLeaveDashboard:
    def __init__(self, hr_client):
        self.hr_client = hr_client

    def get_personal_details(self, employee_id: str) -> Dict:
        try:
            return self.hr_client.fetch_employee_details(employee_id)
        except Exception as e:
            raise LeaveDataSyncError(f"Failed to fetch personal details: {str(e)}")

    def get_leave_balances(self, employee_id: str) -> Dict:
        try:
            return self.hr_client.fetch_leave_balances(employee_id)
        except Exception as e:
            raise LeaveDataSyncError(f"Failed to fetch leave balances: {str(e)}")

    def get_leave_history(self, employee_id: str) -> List[Dict]:
        try:
            return self.hr_client.fetch_leave_history(employee_id)
        except Exception as e:
            raise LeaveDataSyncError(f"Failed to fetch leave history: {str(e)}")
