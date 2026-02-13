"""
Responsive and Usable User Interface
Stub for a responsive, accessible UI layer (CLI demo; replace with real web/mobile frontend).
"""

from lms.employee_dashboard import EmployeeDashboard, Employee, LeaveType

class ResponsiveUI:
    def __init__(self, dashboard: EmployeeDashboard):
        self.dashboard = dashboard
    def render(self):
        print("="*40)
        self.dashboard.display()
        print("(This is a CLI demo. Replace with web/mobile UI for production use.)")

# Example usage
if __name__ == "__main__":
    emp = Employee("u123", "Alice", "alice@company.com", {LeaveType.CASUAL: 10}, [])
    dashboard = EmployeeDashboard(emp)
    ui = ResponsiveUI(dashboard)
    ui.render()
