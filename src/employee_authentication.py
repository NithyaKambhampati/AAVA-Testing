"""
Employee Authentication and Role-Based Access
User Story: As an employee, I want to log in using my organizational credentials, so that I can securely access my leave management features and ensure only authorized users can access the system.
"""

import hashlib
import uuid
from enum import Enum
from typing import Optional

# Simulated user database (in production, integrate with org auth)
USER_DB = {
    'alice@org.com': {'password_hash': hashlib.sha256('alicepass'.encode()).hexdigest(), 'role': 'Employee'},
    'bob@org.com': {'password_hash': hashlib.sha256('bobpass'.encode()).hexdigest(), 'role': 'Manager'},
    'carol@org.com': {'password_hash': hashlib.sha256('carolpass'.encode()).hexdigest(), 'role': 'HR/Admin'},
}

class Role(Enum):
    EMPLOYEE = 'Employee'
    MANAGER = 'Manager'
    HR_ADMIN = 'HR/Admin'

def authenticate(email: str, password: str) -> Optional[dict]:
    """
    Authenticates a user and returns user data if credentials are valid.
    """
    user = USER_DB.get(email)
    if not user:
        return None
    if user['password_hash'] == hashlib.sha256(password.encode()).hexdigest():
        # Generate a session token (simulate)
        return {'email': email, 'role': user['role'], 'session_token': str(uuid.uuid4())}
    return None

def get_accessible_features(role: str) -> list:
    """
    Returns features accessible by the user's role.
    """
    features = {
        Role.EMPLOYEE.value: ['view_own_leave', 'apply_leave', 'view_balance', 'view_history'],
        Role.MANAGER.value: ['view_team_requests', 'approve_reject_leave', 'add_comments'] + ['view_own_leave', 'apply_leave', 'view_balance', 'view_history'],
        Role.HR_ADMIN.value: ['configure_policies', 'manage_holidays', 'view_reports', 'audit_trail'] + ['view_team_requests', 'approve_reject_leave', 'add_comments', 'view_own_leave', 'apply_leave', 'view_balance', 'view_history'],
    }
    return features.get(role, [])

# Example usage with error handling
def login(email: str, password: str):
    user = authenticate(email, password)
    if not user:
        raise PermissionError('Invalid credentials or user not found.')
    print(f"User '{email}' authenticated as {user['role']}. Session: {user['session_token']}")
    features = get_accessible_features(user['role'])
    print(f"Accessible features: {features}")
    return user, features

if __name__ == "__main__":
    try:
        # Simulate login (replace with actual input in production)
        email = 'alice@org.com'
        password = 'alicepass'
        user, features = login(email, password)
    except PermissionError as e:
        print(f"Authentication failed: {e}")
