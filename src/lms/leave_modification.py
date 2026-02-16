"""
Modification and Cancellation of Leave Requests
User Story: As an employee, I want to cancel or modify my leave requests before approval so that I can adjust my plans as needed.
Acceptance Criteria:
- Pending leave requests can be modified or cancelled; follow approval workflow; balances not affected until approval.
"""

from typing import List, Optional

class LeaveRequest:
    def __init__(self, leave_id: str, employee_id: str, status: str = "pending"):
        self.leave_id = leave_id
        self.employee_id = employee_id
        self.status = status
        self.modified = False
        self.cancelled = False

class ModificationService:
    def __init__(self, leave_requests: List[LeaveRequest]):
        self.leave_requests = leave_requests

    def modify(self, leave_id: str, employee_id: str) -> str:
        req = next((r for r in self.leave_requests if r.leave_id == leave_id and r.employee_id == employee_id), None)
        if not req:
            return "Error: Leave request not found."
        if req.status != "pending":
            return "Error: Only pending requests can be modified."
        req.modified = True
        # Should trigger re-approval workflow
        return f"Leave request {leave_id} modified and pending approval."

    def cancel(self, leave_id: str, employee_id: str) -> str:
        req = next((r for r in self.leave_requests if r.leave_id == leave_id and r.employee_id == employee_id), None)
        if not req:
            return "Error: Leave request not found."
        if req.status != "pending":
            return "Error: Only pending requests can be cancelled."
        req.cancelled = True
        req.status = "cancelled"
        return f"Leave request {leave_id} cancelled."

# Example usage:
if __name__ == "__main__":
    reqs = [LeaveRequest("L1", "E123")]
    svc = ModificationService(reqs)
    print(svc.modify("L1", "E123"))
    print(svc.cancel("L1", "E123"))
    print(svc.modify("L1", "E123"))  # Should fail after cancellation
