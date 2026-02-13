"""
Employee Notification of Leave Status Module

As an employee, I want to receive notifications when my leave request is approved or rejected so that I am informed of my leave status in a timely manner.
"""

def send_notification(employee_email, status, comments):
    # Simulate sending a notification (email/SMS)
    print(f"Notification sent to {employee_email}: Your leave request was {status}. Comments: {comments}")

if __name__ == "__main__":
    # Example usage
    send_notification("alice@example.com", "approved", "Enjoy your leave!")
    send_notification("alice@example.com", "rejected", "Insufficient balance.")
