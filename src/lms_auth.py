"""
lms_auth.py
User Authentication via Organizational Credentials
Implements authentication logic for employees, managers, and HR/admin users using organizational credentials (stub for SSO/LDAP integration).
"""

import hashlib
from typing import Optional

# Simulated user database (for demonstration; replace with real integration)
USER_DB = {
    'alice': {'password': 'password123', 'role': 'employee', 'status': 'active'},
    'bob': {'password': 'securepass', 'role': 'manager', 'status': 'active'},
    'carol': {'password': 'adminpass', 'role': 'hr', 'status': 'disabled'},
}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> Optional[dict]:
    """Authenticate user against organizational credentials (stub)."""
    user = USER_DB.get(username)
    if not user:
        return None
    if user['status'] != 'active':
        return None
    # In production, compare hashed passwords and integrate with SSO/LDAP
    if password == user['password']:
        return {'username': username, 'role': user['role']}
    return None

if __name__ == "__main__":
    # Example usage
    test_users = [
        ('alice', 'password123'),
        ('bob', 'wrongpass'),
        ('carol', 'adminpass'),
        ('dave', 'nopass'),
    ]
    for username, password in test_users:
        result = authenticate(username, password)
        if result:
            print(f"Login success: {result['username']} ({result['role']})")
        else:
            print(f"Login failed for user: {username}")
