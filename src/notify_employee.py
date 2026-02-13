"""
Employee Notification of Leave Decisions
As an employee, I want to be notified about approval or rejection of my leave requests, so that I am always aware of my leave status.
"""
class NotificationService:
    def send_notification(self, employee_email, subject, message):
        # Simulate sending email (stub)
        print(f"Sending email to {employee_email}\nSubject: {subject}\nMessage: {message}")
        return {'status': 'success', 'message': 'Notification sent'}

# Example usage
if __name__ == '__main__':
    notifier = NotificationService()
    print(notifier.send_notification('john.doe@company.com', 'Leave Approved', 'Your leave request for 2024-07-01 to 2024-07-02 has been approved.'))
    print(notifier.send_notification('john.doe@company.com', 'Leave Rejected', 'Your leave request for 2024-07-03 to 2024-07-04 has been rejected.'))
