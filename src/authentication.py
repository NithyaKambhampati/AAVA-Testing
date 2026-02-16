# authentication.py
"""
Employee Authentication via Organizational Credentials
Implements SSO/LDAP/Active Directory authentication integration for LMS.
"""
from typing import Optional

class AuthenticationError(Exception):
    pass

class User:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role

class Authenticator:
    def __init__(self, provider: str = 'LDAP'):
        self.provider = provider

    def authenticate(self, username: str, password: str) -> Optional[User]:
        # Placeholder for SSO/LDAP/AD logic
        if not username or not password:
            raise AuthenticationError('Username and password required')
        # Simulate valid credentials
        if username.startswith('emp') and password == 'password123':
            return User(username, 'employee')
        elif username.startswith('mgr') and password == 'password123':
            return User(username, 'manager')
        elif username.startswith('hr') and password == 'password123':
            return User(username, 'hr_admin')
        else:
            raise AuthenticationError('Invalid credentials')

if __name__ == "__main__":
    auth = Authenticator()
    try:
        user = auth.authenticate(input("Username: "), input("Password: "))
        print(f"Welcome, {user.username}! Role: {user.role}")
    except AuthenticationError as e:
        print(f"Authentication failed: {e}")
