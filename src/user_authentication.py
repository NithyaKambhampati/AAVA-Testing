"""
User Authentication Module
As an employee, I want to log in using my organizational credentials, so that I can securely access the Leave Management System.
Acceptance Criteria:
- Valid credentials grant access.
- Invalid credentials deny access with appropriate message.
"""

class UserAuthentication:
 def __init__(self, auth_service):
 self.auth_service = auth_service

 def login(self, username, password):
 if self.auth_service.validate_credentials(username, password):
 return {
 'status': 'success',
 'message': 'Access granted.'
 }
 else:
 return {
 'status': 'failure',
 'message': 'Invalid credentials. Access denied.'
 }

# Example usage:
# auth = UserAuthentication(auth_service)
# result = auth.login('employee1', 'password123')
