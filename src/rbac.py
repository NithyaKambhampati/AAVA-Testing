"""
Role-Based Access Control
As a user, I want access to system features and data to be restricted based on my role so that confidentiality and security are maintained.
"""

class RBACService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def has_access(self, user_id: int, permission: str) -> bool:
        role = self.user_repo.get_role(user_id)
        # Define role-permission mapping
        role_permissions = {
            'employee': {'view_dashboard', 'apply_leave', 'modify_leave'},
            'manager': {'view_dashboard', 'approve_leave', 'view_team_leaves'},
            'hr_admin': {'view_dashboard', 'configure_policy', 'view_reports', 'audit_trail'}
        }
        return permission in role_permissions.get(role, set())
