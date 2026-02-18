"""
Notifications for Leave Actions
As an employee or manager, I want to receive notifications for approval or rejection actions so that I am promptly informed of leave status updates.
"""

from typing import List, Dict
import random

NOTIFICATIONS: List[Dict] = []

class NotificationError(Exception):
    pass

def send_notification(user_id: str, notification_type: str, channel: str, message: str):
    # Simulate notification delivery and error handling
    if channel not in ['email', 'sms', 'in-app']:
        raise NotificationError('Unsupported notification channel.')
    # Simulate delivery failure
    if random.choice([True, False]):
        NOTIFICATIONS.append({'user_id': user_id, 'type': notification_type, 'channel': channel, 'status': 'sent', 'message': message})
        print(f"Notification sent to {user_id} via {channel}: {message}")
    else:
        NOTIFICATIONS.append({'user_id': user_id, 'type': notification_type, 'channel': channel, 'status': 'failed', 'message': message})
        print(f"Notification failed for {user_id} via {channel}")

# Example usage
if __name__ == '__main__':
    try:
        send_notification('employee1', 'leave_approved', 'email', 'Your leave has been approved.')
        send_notification('manager1', 'new_leave_request', 'sms', 'New leave request submitted.')
    except NotificationError as e:
        print(str(e))
    print('Notification log:', NOTIFICATIONS)
