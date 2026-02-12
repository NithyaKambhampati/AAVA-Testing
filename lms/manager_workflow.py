# lms/manager_workflow.py
"""
Manager approval workflow for leave requests.
"""
from typing import List, Dict

def get_pending_requests(manager_id: str, team_requests: List[Dict]) -> List[Dict]:
 return [req for req in team_requests if req['status'] == 'Pending' and req['manager_id'] == manager_id]

def approve_leave_request(request: Dict, manager_comments: str = ""):
 request['status'] = 'Approved'
 request['manager_comments'] = manager_comments
 request['actioned_by'] = 'manager'
 notify_employee(request, approved=True)

def reject_leave_request(request: Dict, manager_comments: str = ""):
 request['status'] = 'Rejected'
 request['manager_comments'] = manager_comments
 request['actioned_by'] = 'manager'
 notify_employee(request, approved=False)

def notify_employee(request: Dict, approved: bool):
 # Placeholder for notification logic (email/SMS/etc)
 status = 'approved' if approved else 'rejected'
 print(f"Notification: Your leave request from {request['start_date']} to {request['end_date']} has been {status}.")
