"""
Data Security and Access Control
User Story: As a system user, I want data security and access control enforced, so that only authorized users can view or act on relevant leave information.
"""

from typing import List, Dict

# Simulated user and role data
USERS = {
    'alice@org.com': 'Employee',
    'bob@org.com': 'Manager',
    'carol@org.com': 'HR/Admin',
}

LEAVE_REQUESTS = [
    {'request_id': 1, 'email': 'alice@org.com', 'leave_type': 'Sick Leave', 'status': 'Approved'},
    {'request_id': 2, 'email': 'bob@org.com', 'leave_type': 'Casual Leave', 'status': 'Pending'},
]


def get_leave_data(requesting_user: str) -> List[Dict]:
    role = USERS.get(requesting_user)
    if role == 'Employee':
        # Only own data
        return [req for req in LEAVE_REQUESTS if req['email'] == requesting_user]
    elif role == 'Manager':
        # See team and own data (simulate as all requests for demo)
        return LEAVE_REQUESTS
    elif role == 'HR/Admin':
        # See all data
        return LEAVE_REQUESTS
    else:
        raise PermissionError('Unauthorized access')


def access_attempt(email: str, target_email: str) -> bool:
    if email == target_email or USERS.get(email) in ['Manager', 'HR/Admin']:
        return True
    else:
        # Log unauthorized access
        print(f"Unauthorized access attempt by {email} to {target_email}'s data.")
        return False

if __name__ == "__main__":
    # Alice tries to view her data
    print(get_leave_data('alice@org.com'))
    # Bob (manager) views all
    print(get_leave_data('bob@org.com'))
    # Carol (HR/Admin) views all
    print(get_leave_data('carol@org.com'))
    # Unauthorized attempt
    print(access_attempt('alice@org.com', 'bob@org.com'))
