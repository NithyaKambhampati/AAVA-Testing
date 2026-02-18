# dashboard.py

from typing import List, Dict

class EmployeeDashboard:
    def __init__(self, user_id: str, leave_balances: Dict[str, int], leave_history: List[Dict]):
        self.user_id = user_id
        self.leave_balances = leave_balances  # e.g., {'sick': 5, 'casual': 7}
        self.leave_history = leave_history    # List of leave requests

    def get_personal_details(self):
        # Placeholder for fetching personal details
        return {"user_id": self.user_id, "name": "John Doe"}

    def get_leave_balances(self):
        return self.leave_balances

    def get_leave_history(self):
        return self.leave_history

    def update_leave_balance(self, leave_type: str, delta: int):
        if leave_type in self.leave_balances:
            self.leave_balances[leave_type] += delta

# Example usage
if __name__ == "__main__":
    balances = {'sick': 5, 'casual': 7}
    history = [
        {"type": "sick", "start": "2024-06-01", "end": "2024-06-03", "status": "approved"},
        {"type": "casual", "start": "2024-05-15", "end": "2024-05-16", "status": "rejected"}
    ]
    dashboard = EmployeeDashboard("emp001", balances, history)
    print(dashboard.get_personal_details())
    print(dashboard.get_leave_balances())
    print(dashboard.get_leave_history())
