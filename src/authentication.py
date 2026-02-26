"""
User Authentication with Organizational Credentials
As an employee or manager, I want to log in to the LMS using my organizational credentials so that I can securely access my leave management features.
"""

from typing import Optional

class AuthService:
    def __init__(self, org_auth_adapter):
        self.org_auth_adapter = org_auth_adapter

    def login(self, username: str, password: str) -> Optional[dict]:
        """
        Authenticate against the organizational authentication provider.
        Returns user profile dict if successful, else None.
        """
        if not username or not password:
            return None
        user = self.org_auth_adapter.authenticate(username, password)
        if user:
            return user
        return None

    def is_authenticated(self, session_token: str) -> bool:
        return self.org_auth_adapter.validate_session(session_token)
