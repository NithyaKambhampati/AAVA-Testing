# lms/authentication.py
"""
Handles employee authentication using organizational credentials.
"""

class AuthenticationError(Exception):
 pass

def authenticate_employee(username: str, password: str) -> bool:
 """
 Authenticates an employee.
 Returns True if credentials are valid, else raises AuthenticationError.
 """
 # Placeholder for real authentication logic (e.g., LDAP/SSO)
 if username == "employee" and password == "password123":
 return True
 else:
 raise AuthenticationError("Invalid credentials. Access denied.")
