"""
Role-Based Access Control
User Story: As the LMS, I want to restrict user access to relevant information and actions based on their role so that data privacy and security are maintained.
Acceptance Criteria:
- User denied access to data/actions outside their role.
"""

class RBACService:
    def __init__(self, role_permissions):
        self.role_permissions = role_permissions  # role -> set of allowed actions

    def check_access(self, role: str, action: str) -> bool:
        return action in self.role_permissions.get(role, set())

# Example usage:
if __name__ == "__main__":
    permissions = {
        "employee": {"view_dashboard", "apply_leave", "cancel_leave"},
        "manager": {"approve_leave", "view_team"},
        "hr_admin": {"configure_policy", "view_reports", "audit_logs"}
    }
    rbac = RBACService(permissions)
    print(rbac.check_access("employee", "apply_leave"))  # True
    print(rbac.check_access("employee", "approve_leave"))  # False
    print(rbac.check_access("hr_admin", "audit_logs"))  # True
