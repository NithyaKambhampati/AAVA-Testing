"""
Notifications for Leave Actions
Sends notifications to employees upon approval, rejection, or cancellation of leave requests. Includes retry and logging.
"""

from datetime import datetime
from typing import List

class Notification:
    def __init__(self, to: str, subject: str, body: str):
        self.to = to
        self.subject = subject
        self.body = body
        self.sent_at = None
        self.status = "pending"

class NotificationService:
    def __init__(self):
        self.log: List[Notification] = []
    def send(self, notification: Notification, retry: int = 3):
        for attempt in range(retry):
            try:
                # Simulate sending (replace with email/SMS integration)
                notification.sent_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                notification.status = "sent"
                self.log.append(notification)
                print(f"Notification sent to {notification.to}: {notification.subject}")
                return True
            except Exception as e:
                notification.status = f"failed: {str(e)}"
                print(f"Notification failed (attempt {attempt + 1}): {str(e)}")
        self.log.append(notification)
        return False

# Example usage
if __name__ == "__main__":
    svc = NotificationService()
    n = Notification("alice@company.com", "Leave Approved", "Your leave has been approved.")
    svc.send(n)
