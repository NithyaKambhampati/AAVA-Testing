"""
Employee Secure Login Module

As an employee, I want to securely log in to the Leave Management System using my organizational credentials so that I can access my leave details and perform leave-related actions.
"""

import hashlib
from typing import Optional

class AuthenticationError(Exception):
    pass

def authenticate_employee(username: str, password: str, org_auth_func) -> bool:
    """
    Authenticates an employee using the organization's authentication system.
    Args:
        username (str): Employee's username
        password (str): Employee's password
        org_auth_func (callable): Function to validate credentials with org system
    Returns:
        bool: True if credentials are valid, False otherwise
    Raises:
        AuthenticationError: If credentials are invalid
    """
    if not username or not password:
        raise AuthenticationError("Username and password are required.")
    try:
        if org_auth_func(username, password):
            return True
        else:
            raise AuthenticationError("Invalid credentials.")
    except Exception as e:
        raise AuthenticationError(f"Authentication system error: {e}")

if __name__ == "__main__":
    # Example usage with a mock org_auth_func
    def mock_org_auth_func(username, password):
        # Simulate org authentication (replace with real integration)
        return username == "employee1" and password == "password123"
    try:
        result = authenticate_employee("employee1", "password123", mock_org_auth_func)
        print("Login successful!" if result else "Login failed!")
    except AuthenticationError as e:
        print(f"Login error: {e}")
