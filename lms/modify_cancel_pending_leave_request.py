"""
Modify/Cancel Pending Leave Request Module
- Allows employees to modify or cancel pending leave requests
- Ensures workflow is re-triggered or request is removed as appropriate
- Handles rollback on system failure
"""

class LeaveModificationError(Exception):
    pass

class LeaveModificationService:
    def __init__(self, hr_client):
        self.hr_client = hr_client

    def modify_leave_request(self, employee_id: str, leave_request_id: str, new_data: dict) -> dict:
        leave_request = self.hr_client.fetch_leave_request(leave_request_id)
        if leave_request['employee_id'] != employee_id or leave_request['status'] != 'REQUESTED':
            raise LeaveModificationError("Modification not allowed.")
        try:
            self.hr_client.update_leave_request(leave_request_id, new_data)
            self.hr_client.update_leave_status(leave_request_id, 'MODIFIED')
            return {'status':'MODIFIED', 'leave_request_id':leave_request_id}
        except Exception as e:
            # Rollback logic
            self.hr_client.rollback_leave_request(leave_request_id)
            raise LeaveModificationError(f"Modification failed: {str(e)}")

    def cancel_leave_request(self, employee_id: str, leave_request_id: str) -> dict:
        leave_request = self.hr_client.fetch_leave_request(leave_request_id)
        if leave_request['employee_id'] != employee_id or leave_request['status'] != 'REQUESTED':
            raise LeaveModificationError("Cancellation not allowed.")
        try:
            self.hr_client.update_leave_status(leave_request_id, 'CANCELLED')
            return {'status':'CANCELLED', 'leave_request_id':leave_request_id}
        except Exception as e:
            self.hr_client.rollback_leave_request(leave_request_id)
            raise LeaveModificationError(f"Cancellation failed: {str(e)}")
