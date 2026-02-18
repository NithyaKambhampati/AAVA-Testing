"""
User Authentication and Role-Based Access
As an employee, manager, or HR/Admin, I want to log in using my organizational credentials so that I can securely access the Leave Management System and perform actions according to my role.
"""

import hashlib
from typing import Dict, Optional

# Mock user database
USER_DB = {
    'employee1': {'password': 'pass123', 'role': 'employee'},
    'manager1': {'password': 'pass456', 'role': 'manager'},
    'hradmin1': {'password': 'pass789', 'role': 'hradmin'},
}

class AuthenticationError(Exception):
    pass

class AuthorizationError(Exception):
    pass

def login(username: str, password: str) -> Dict[str, str]:
    user = USER_DB.get(username)
    if user and user['password'] == password:
        return {'username': username, 'role': user['role']}
    raise AuthenticationError('Invalid credentials, access denied.')

def get_role_access(role: str) -> Dict[str, bool]:
    access = {
        'employee': {'dashboard': True, 'apply_leave': True, 'manager_dashboard': False, 'admin_config': False},
        'manager': {'dashboard': True, 'apply_leave': True, 'manager_dashboard': True, 'admin_config': False},
        'hradmin': {'dashboard': True, 'apply_leave': True, 'manager_dashboard': True, 'admin_config': True},
    }
    return access.get(role, {})

# Edge case: Unauthorized access attempts must be logged and prevented.
def log_unauthorized_access(username: str):
    print(f"Unauthorized access attempt by {username}")

# Example usage
if __name__ == '__main__':
    try:
        user_info = login('employee1', 'pass123')
        access = get_role_access(user_info['role'])
        print(f"Login successful. Role: {user_info['role']}, Access: {access}")
    except AuthenticationError as e:
        log_unauthorized_access('employee1')
        print(str(e))
