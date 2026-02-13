"""
Leave Reporting and Analytics
User Story: As an HR/Admin, I want to view leave reports and analytics, so that I can monitor leave trends, pending approvals, and compliance across teams and the organization.
"""

from typing import List, Dict
from collections import Counter, defaultdict

# Simulated leave data
LEAVE_REQUESTS = [
    {'employee': 'alice@org.com', 'team': 'Team A', 'leave_type': 'Sick Leave', 'status': 'Approved', 'start_date': '2024-06-10', 'end_date': '2024-06-12'},
    {'employee': 'bob@org.com', 'team': 'Team A', 'leave_type': 'Casual Leave', 'status': 'Pending', 'start_date': '2024-07-01', 'end_date': '2024-07-02'},
    {'employee': 'carol@org.com', 'team': 'Team B', 'leave_type': 'Earned Leave', 'status': 'Rejected', 'start_date': '2024-07-10', 'end_date': '2024-07-12'},
]


def leave_report_by_team() -> Dict[str, int]:
    report = defaultdict(int)
    for req in LEAVE_REQUESTS:
        report[req['team']] += 1
    return dict(report)

def pending_approvals() -> List[Dict]:
    return [req for req in LEAVE_REQUESTS if req['status'] == 'Pending']

def leave_trends() -> Dict[str, int]:
    c = Counter(req['leave_type'] for req in LEAVE_REQUESTS)
    return dict(c)

if __name__ == "__main__":
    print("Leave counts by team:", leave_report_by_team())
    print("Pending approvals:", pending_approvals())
    print("Leave type trends:", leave_trends())
