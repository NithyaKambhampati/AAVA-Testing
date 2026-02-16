"""
Employee Dashboard Access
User Story: As an employee, I want to view my dashboard with personal details, leave balances, and leave history so that I can track my leave status.
Acceptance Criteria:
- Logged-in employee sees accurate personal details, leave balances, and leave history.
"""

from typing import List, Dict

class Employee:
    def __init__(self, id: str, name: str, leave_balances: Dict[str, int], leave_history: List[Dict]):
        self.id = id
        self.name = name
        self.leave_balances = leave_balances
        self.leave_history = leave_history

class DashboardService:
    def __init__(self, employee_db):
        self.employee_db = employee_db  # dict: id -> Employee

    def get_dashboard(self, employee_id: str) -> str:
        if employee_id not in self.employee_db:
            return "Error: Employee not found."
        emp = self.employee_db[employee_id]
        dashboard = f"Employee: {emp.name}\nLeave Balances: {emp.leave_balances}\nLeave History:"
        for leave in emp.leave_history:
            dashboard += f"\n- {leave}"
        return dashboard

# Example usage:
if __name__ == "__main__":
    leave_balances = {"casual": 5, "sick": 8, "earned": 10}
    leave_history = [
        {"type": "casual", "dates": "2024-06-01 to 2024-06-02", "status": "approved"},
        {"type": "sick", "dates": "2024-05-15", "status": "rejected"}
    ]
    employee_db = {
        "E123": Employee("E123", "Alice", leave_balances, leave_history)
    }
    dashboard = DashboardService(employee_db)
    print(dashboard.get_dashboard("E123"))
