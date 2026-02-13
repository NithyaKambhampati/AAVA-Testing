"""
Manager Dashboard Module
- Managers can view all leave requests from their team and take actions
"""

from typing import List, Dict

TEAM_LEAVE_REQUESTS = [
    {'id': 1, 'employee': 'alice@company.com', 'type': 'CASUAL', 'start': '2024-06-10', 'end': '2024-06-12', 'status': 'PENDING', 'manager': 'bob@company.com'},
    {'id': 2, 'employee': 'eve@company.com', 'type': 'SICK', 'start': '2024-06-15', 'end': '2024-06-16', 'status': 'APPROVED', 'manager': 'bob@company.com'},
    {'id': 3, 'employee': 'alice@company.com', 'type': 'EARNED', 'start': '2024-06-20', 'end': '2024-06-22', 'status': 'REJECTED', 'manager': 'bob@company.com'},
]


def get_team_requests(manager_email: str) -> List[Dict]:
    return [req for req in TEAM_LEAVE_REQUESTS if req['manager'] == manager_email]

if __name__ == "__main__":
    manager_email = input("Manager Email: ")
    requests = get_team_requests(manager_email)
    print(f"Leave Requests for {manager_email}:")
    for req in requests:
        print(req)
