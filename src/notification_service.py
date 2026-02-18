# notification_service.py

from datetime import datetime
from typing import List, Dict

class NotificationService:
    def __init__(self):
        self.notifications = []

    def notify(self, user_id: str, message: str, notification_type: str = "in-app"):
        notif = {
            "user_id": user_id,
            "message": message,
            "type": notification_type,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.notifications.append(notif)
        return notif

    def get_notifications(self, user_id: str) -> List[Dict]:
        return [n for n in self.notifications if n['user_id'] == user_id]

# Example usage
if __name__ == "__main__":
    service = NotificationService()
    service.notify("emp001", "Your leave request was approved.")
    service.notify("emp002", "Your leave request was rejected.")
    service.notify("emp001", "Your leave request was modified.")
    print(service.get_notifications("emp001"))
