"""
Reporting and Analytics for HR/Admin
User Story: As an HR/admin, I want to generate organization-wide leave reports and trends so that I can monitor usage and compliance.
Acceptance Criteria:
- Reports generated with accurate leave data (total taken, trends, pending approvals), exportable.
"""

from typing import List, Dict

class LeaveRequest:
    def __init__(self, employee_id: str, leave_type: str, start_date: str, end_date: str, status: str):
        self.employee_id = employee_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

class ReportingService:
    def __init__(self, leave_requests: List[LeaveRequest]):
        self.leave_requests = leave_requests

    def total_leave_taken(self) -> Dict[str, int]:
        totals = {}
        for req in self.leave_requests:
            if req.status == "approved":
                totals[req.leave_type] = totals.get(req.leave_type, 0) + 1
        return totals

    def pending_approvals(self) -> int:
        return sum(1 for req in self.leave_requests if req.status == "pending")

    def leave_trends(self) -> Dict[str, int]:
        # For simplicity, count per month (YYYY-MM)
        trends = {}
        for req in self.leave_requests:
            month = req.start_date[:7]
            trends[month] = trends.get(month, 0) + 1
        return trends

# Example usage:
if __name__ == "__main__":
    reqs = [
        LeaveRequest("E123", "casual", "2024-06-10", "2024-06-12", "approved"),
        LeaveRequest("E124", "sick", "2024-06-11", "2024-06-11", "pending"),
        LeaveRequest("E125", "casual", "2024-05-20", "2024-05-21", "approved")
    ]
    svc = ReportingService(reqs)
    print("Total leave taken:", svc.total_leave_taken())
    print("Pending approvals:", svc.pending_approvals())
    print("Leave trends:", svc.leave_trends())
