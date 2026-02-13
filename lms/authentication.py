"""
User Authentication and Role-Based Access
Implements secure login using organizational credentials and enforces role-based access control.
"""

from enum import Enum
from typing import Optional, Dict

class Role(Enum):
    EMPLOYEE = "employee"
    MANAGER = "manager"
    HR_ADMIN = "hr_admin"

class User:
    def __init__(self, user_id: str, name: str, role: Role):
        self.user_id = user_id
        self.name = name
        self.role = role

class AuthenticationError(Exception):
    pass

class AuthorizationError(Exception):
    pass

class AuthService:
    def __init__(self, credential_provider):
        self.credential_provider = credential_provider

    def login(self, username: str, password: str) -> User:
        user_info = self.credential_provider.authenticate(username, password)
        if not user_info:
            raise AuthenticationError("Invalid credentials")
        return User(user_info["user_id"], user_info["name"], Role(user_info["role"]))

    def enforce_role(self, user: User, allowed_roles):
        if user.role not in allowed_roles:
            raise AuthorizationError(f"Access denied for role: {user.role}")

# Example credential provider stub
class CredentialProvider:
    def authenticate(self, username, password) -> Optional[Dict]:
        # Replace with SSO or directory integration
        # For demo: username==password, role based on username
        roles = {"employee": Role.EMPLOYEE, "manager": Role.MANAGER, "hr_admin": Role.HR_ADMIN}
        if username == password and username in roles:
            return {"user_id": username, "name": username.capitalize(), "role": roles[username].value}
        return None

# Example usage
if __name__ == "__main__":
    cp = CredentialProvider()
    auth = AuthService(cp)
    try:
        user = auth.login("employee", "employee")
        print(f"Logged in as: {user.name} ({user.role})")
        auth.enforce_role(user, [Role.EMPLOYEE, Role.MANAGER])
    except (AuthenticationError, AuthorizationError) as e:
        print(str(e))
