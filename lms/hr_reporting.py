"""
HR/Admin: Organization and Team Leave Reporting
Generates summary and detailed leave usage, trends, and pending approvals.
"""

from typing import List, Dict
from lms.employee_dashboard import Employee, LeaveRequest

class HRReporting:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    def summary_report(self) -> Dict:
        usage = {}
        for emp in self.employees:
            for req in emp.leave_history:
                usage.setdefault(req.leave_type, 0)
                if req.status == "Approved":
                    sd = req.start_date
                    ed = req.end_date
                    days = (int(ed[-2:]) - int(sd[-2:])) + 1  # Simplified for demo
                    usage[req.leave_type] += days
        return usage

    def pending_approvals(self) -> List[Dict]:
        pending = []
        for emp in self.employees:
            for req in emp.leave_history:
                if req.status == "Pending":
                    pending.append({
                        "employee": emp.name,
                        "leave_type": req.leave_type,
                        "start_date": req.start_date,
                        "end_date": req.end_date,
                        "reason": req.reason
                    })
        return pending

    def trend_report(self) -> Dict:
        # Example: count leaves per month
        trends = {}
        for emp in self.employees:
            for req in emp.leave_history:
                if req.status == "Approved":
                    month = req.start_date[:7]  # YYYY-MM
                    trends.setdefault(month, 0)
                    trends[month] += 1
        return trends

# Example usage
if __name__ == "__main__":
    from lms.employee_dashboard import LeaveType
    emp1 = Employee("u123", "Alice", "alice@company.com", {LeaveType.CASUAL: 10}, [])
    emp2 = Employee("u124", "Bob", "bob@company.com", {LeaveType.SICK: 5}, [])
    hr = HRReporting([emp1, emp2])
    print("Summary:", hr.summary_report())
    print("Pending Approvals:", hr.pending_approvals())
    print("Trends:", hr.trend_report())
