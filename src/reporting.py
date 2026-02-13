"""
Reporting Module
- HR/Admin can access reports on leave taken, trends, and pending approvals
- Includes rapid succession of requests
"""

from typing import List, Dict

LEAVE_REQUESTS = [
    {'id': 1, 'employee': 'alice@company.com', 'type': 'CASUAL', 'start': '2024-06-10', 'end': '2024-06-12', 'status': 'APPROVED'},
    {'id': 2, 'employee': 'eve@company.com', 'type': 'SICK', 'start': '2024-06-15', 'end': '2024-06-16', 'status': 'PENDING'},
    {'id': 3, 'employee': 'alice@company.com', 'type': 'EARNED', 'start': '2024-06-20', 'end': '2024-06-22', 'status': 'REJECTED'},
]


def leave_summary() -> Dict:
    summary = {}
    for req in LEAVE_REQUESTS:
        summary.setdefault(req['employee'], []).append(req)
    return summary

def pending_approvals() -> List[Dict]:
    return [req for req in LEAVE_REQUESTS if req['status'] == 'PENDING']

def leave_trends() -> Dict:
    trends = {}
    for req in LEAVE_REQUESTS:
        trends.setdefault(req['type'], 0)
        trends[req['type']] += 1
    return trends

def export_report() -> str:
    # Simulate CSV export
    csv_lines = ['id,employee,type,start,end,status']
    for req in LEAVE_REQUESTS:
        csv_lines.append(f"{req['id']},{req['employee']},{req['type']},{req['start']},{req['end']},{req['status']}")
    return '\n'.join(csv_lines)

if __name__ == "__main__":
    print("Leave Summary:", leave_summary())
    print("Pending Approvals:", pending_approvals())
    print("Leave Trends:", leave_trends())
    print("CSV Export:\n", export_report())
