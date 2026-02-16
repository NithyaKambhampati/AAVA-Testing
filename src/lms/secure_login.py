"""
Secure Login for All Users
User Story: As an employee, manager, or HR/admin, I want to log into the LMS using my organizational credentials so that my access is secure and role-based.
Acceptance Criteria:
- Valid credentials grant access with correct role-based dashboard.
- Invalid credentials are denied with error message.
"""

from typing import Optional

class User:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role

class AuthService:
    def __init__(self, credential_db):
        self.credential_db = credential_db  # dict: username -> (password, role)

    def login(self, username: str, password: str) -> Optional[User]:
        if username in self.credential_db:
            stored_pw, role = self.credential_db[username]
            if password == stored_pw:
                return User(username, password, role)
        return None

    def get_dashboard(self, user: Optional[User]) -> str:
        if user is None:
            return "Error: Invalid credentials. Access denied."
        return f"Welcome {user.username}! Role: {user.role}"

# Example usage:
if __name__ == "__main__":
    credential_db = {
        "alice": ("alicepw", "employee"),
        "bob": ("bobpw", "manager"),
        "carol": ("carolpw", "hr_admin")
    }
    auth = AuthService(credential_db)
    user = auth.login("alice", "alicepw")
    print(auth.get_dashboard(user))  # Should show employee dashboard
    invalid_user = auth.login("alice", "wrongpw")
    print(auth.get_dashboard(invalid_user))  # Should show error message
