"""
Notification Module
- Notifies employees on leave approval/rejection
- Handles retry logic for notification failures
"""

import time
from typing import Dict, List

NOTIFICATION_QUEUE = []
DELIVERY_LOG = []


def send_notification(to: str, message: str) -> bool:
    # Simulate random delivery failure
    import random
    success = random.choice([True, True, True, False])  # 75% success
    if success:
        DELIVERY_LOG.append({'to': to, 'message': message, 'status': 'SENT'})
        return True
    else:
        DELIVERY_LOG.append({'to': to, 'message': message, 'status': 'FAILED'})
        return False

def notify_employee(to: str, message: str, retries: int = 3):
    for attempt in range(1, retries + 1):
        if send_notification(to, message):
            print(f"Notification sent to {to} on attempt {attempt}.")
            return True
        else:
            print(f"Notification to {to} failed on attempt {attempt}. Retrying...")
            time.sleep(1)  # Simulate retry delay
    print(f"Notification to {to} failed after {retries} attempts.")
    return False

if __name__ == "__main__":
    print("Sending notification...")
    notify_employee('alice@company.com', 'Your leave request has been approved!')
    print("Delivery Log:", DELIVERY_LOG)
