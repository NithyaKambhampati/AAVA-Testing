"""
Employee Notification of Leave Decisions
As an employee, I want to receive notifications when my leave request is approved or rejected so that I am promptly informed of the outcome.
"""
import time

class NotificationService:
    def __init__(self, email_adapter, sms_adapter=None):
        self.email_adapter = email_adapter
        self.sms_adapter = sms_adapter

    def notify_employee(self, user_id: int, status: str, comment: str = ""):
        # Retrieve employee contact info (not implemented)
        message = f"Your leave request has been {status}. {comment}"
        self.email_adapter.send_email(user_id, message)
        if self.sms_adapter:
            self.sms_adapter.send_sms(user_id, message)
        # Simulate notification within 1 minute
        time.sleep(1)
        return True
