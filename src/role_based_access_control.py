"""
Role-Based Access Control Module
- Enforces access to data/actions based on user role (employee, manager, HR/Admin)
"""

from typing import Dict

ROLE_PERMISSIONS = {
    'employee': ['view_dashboard', 'apply_leave', 'modify_leave', 'cancel_leave'],
    'manager': ['view_team_requests', 'approve_leave', 'reject_leave'],
    'hr': ['configure_system', 'view_reports', 'audit_logs'],
}


def has_permission(role: str, action: str) -> bool:
    return action in ROLE_PERMISSIONS.get(role, [])

if __name__ == "__main__":
    print("Employee permissions:", ROLE_PERMISSIONS['employee'])
    print("Manager permissions:", ROLE_PERMISSIONS['manager'])
    print("HR permissions:", ROLE_PERMISSIONS['hr'])
    print("Can employee approve leave?", has_permission('employee', 'approve_leave'))
    print("Can manager approve leave?", has_permission('manager', 'approve_leave'))
