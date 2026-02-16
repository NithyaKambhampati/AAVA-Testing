# manager_approval.py
"""
Manager Approval Workflow for Leave Requests
Allows managers to review, approve, or reject leave requests and notify employees.
"""
from typing import List, Dict

class ManagerApprovalError(Exception):
    pass

class LeaveRequest:
    def __init__(self, request_id: str, employee: str, leave_type: str, start_date: str, end_date: str, status: str, reason: str = ""):
        self.request_id = request_id
        self.employee = employee
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.reason = reason
        self.comments = ""

class Manager:
    def __init__(self, name: str, team_requests: List[LeaveRequest]):
        self.name = name
        self.team_requests = team_requests

    def review_requests(self):
        for req in self.team_requests:
            print(f"Request {req.request_id}: {req.employee} wants {req.leave_type} from {req.start_date} to {req.end_date} ({req.status}). Reason: {req.reason}")

    def approve_request(self, request_id: str, comments: str = ""):
        for req in self.team_requests:
            if req.request_id == request_id and req.status == "Pending":
                req.status = "Approved"
                req.comments = comments
                self.notify_employee(req, "approved")
                return f"Request {request_id} approved"
        raise ManagerApprovalError("Request not found or not pending")

    def reject_request(self, request_id: str, comments: str = ""):
        for req in self.team_requests:
            if req.request_id == request_id and req.status == "Pending":
                req.status = "Rejected"
                req.comments = comments
                self.notify_employee(req, "rejected")
                return f"Request {request_id} rejected"
        raise ManagerApprovalError("Request not found or not pending")

    def notify_employee(self, req: LeaveRequest, action: str):
        print(f"Notification: {req.employee}, your leave request ({req.request_id}) was {action}. Comments: {req.comments}")

if __name__ == "__main__":
    requests = [
        LeaveRequest("L123", "emp001", "Casual", "2024-06-10", "2024-06-12", "Pending", "Family event"),
        LeaveRequest("L124", "emp002", "Sick", "2024-06-15", "2024-06-16", "Pending", "Fever")
    ]
    mgr = Manager("Bob Manager", requests)
    mgr.review_requests()
    try:
        print(mgr.approve_request("L123", "Approved, ensure backup"))
        print(mgr.reject_request("L124", "Insufficient coverage"))
    except ManagerApprovalError as e:
        print(f"Error: {e}")
