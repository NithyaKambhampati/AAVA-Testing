"""
Manager Leave Approval Workflow Module

As a manager, I want to view and act on leave requests from my team in a dashboard so that I can efficiently approve or reject requests with comments.
"""

class ApprovalError(Exception):
    pass

class LeaveRequest:
    def __init__(self, request_id, employee, leave_type, start_date, end_date, status, comments=""):
        self.request_id = request_id
        self.employee = employee
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.comments = comments

class Manager:
    def __init__(self, manager_id, name, team_requests):
        self.manager_id = manager_id
        self.name = name
        self.team_requests = team_requests # List[LeaveRequest]

    def view_requests(self):
        return [req for req in self.team_requests if req.status == "Pending"]

    def act_on_request(self, request_id, approve, comments=""):
        for req in self.team_requests:
            if req.request_id == request_id:
                if req.status != "Pending":
                    raise ApprovalError("Request is not pending.")
                req.status = "Approved" if approve else "Rejected"
                req.comments = comments
                # Simulate employee notification
                print(f"Employee notified: Leave request {request_id} {req.status.lower()} with comments: {comments}")
                return req
        raise ApprovalError("Leave request not found.")

if __name__ == "__main__":
    # Example usage
    reqs = [LeaveRequest(1, "Alice", "Casual", "2024-07-01", "2024-07-05", "Pending")]
    mgr = Manager(2001, "Bob", reqs)
    pending = mgr.view_requests()
    print("Pending requests:", [vars(r) for r in pending])
    try:
        mgr.act_on_request(1, True, "Enjoy your leave!")
    except ApprovalError as e:
        print(f"Approval error: {e}")
