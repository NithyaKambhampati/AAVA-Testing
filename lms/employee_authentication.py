"""
Employee Authentication Module
- Handles login via organizational credentials
- Enforces role-based access control
- Integrates with SSO/LDAP
"""

from typing import Optional

class AuthenticationError(Exception):
    pass

class EmployeeAuthenticator:
    def __init__(self, sso_client):
        self.sso_client = sso_client

    def authenticate(self, username: str, password: str) -> dict:
        """
        Authenticate user with organizational SSO/LDAP credentials.
        Returns user info dict if successful, else raises AuthenticationError.
        """
        try:
            user = self.sso_client.login(username, password)
            if not user or not user.get('role'):
                raise AuthenticationError("Invalid credentials or missing role.")
            return user
        except Exception as e:
            raise AuthenticationError(f"Authentication failed: {str(e)}")

    def get_user_role(self, user: dict) -> Optional[str]:
        return user.get('role') if user else None
