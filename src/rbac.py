# rbac.py

from typing import Dict
from datetime import datetime

class RBAC:
    def __init__(self, user_roles: Dict[str, str]):
        self.user_roles = user_roles  # {'emp001': 'employee', 'mgr001': 'manager', 'admin001': 'hr_admin'}
        self.audit_log = []

    def check_access(self, user_id: str, feature: str) -> bool:
        role = self.user_roles.get(user_id)
        permitted_features = {
            'employee': ['dashboard', 'apply_leave', 'modify_leave', 'cancel_leave'],
            'manager': ['dashboard', 'approve_leave', 'reject_leave', 'team_reports'],
            'hr_admin': ['dashboard', 'configure', 'reports', 'audit_logs', 'override_balances']
        }
        has_access = feature in permitted_features.get(role, [])
        self._log_action(user_id, role, feature, has_access)
        return has_access

    def _log_action(self, user_id: str, role: str, feature: str, result: bool):
        self.audit_log.append({
            "user_id": user_id,
            "role": role,
            "feature": feature,
            "access_granted": result,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_audit_log(self):
        return self.audit_log

# Example usage
if __name__ == "__main__":
    roles = {'emp001': 'employee', 'mgr001': 'manager', 'admin001': 'hr_admin'}
    rbac = RBAC(roles)
    print(rbac.check_access('emp001', 'apply_leave'))
    print(rbac.check_access('mgr001', 'approve_leave'))
    print(rbac.check_access('admin001', 'audit_logs'))
    print(rbac.check_access('emp001', 'audit_logs'))
    print(rbac.get_audit_log())
