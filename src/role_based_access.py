"""
Role-Based Access Control
As the system, I want to restrict data and actions by user role, so that only authorized users can perform specific actions.
"""
class RBAC:
    def __init__(self):
        self.roles = {'employee': set(), 'manager': set(), 'hr_admin': set()}
        self.permissions = {
            'employee': {'view_dashboard', 'apply_leave', 'modify_leave'},
            'manager': {'view_team', 'approve_leave', 'reject_leave'},
            'hr_admin': {'configure_policies', 'view_reports'}
        }

    def assign_role(self, user_id, role):
        if role in self.roles:
            self.roles[role].add(user_id)

    def has_permission(self, user_id, permission):
        for role, users in self.roles.items():
            if user_id in users and permission in self.permissions[role]:
                return True
        return False

# Example usage
if __name__ == '__main__':
    rbac = RBAC()
    rbac.assign_role('E123', 'employee')
    rbac.assign_role('M456', 'manager')
    rbac.assign_role('H789', 'hr_admin')
    print(rbac.has_permission('E123', 'apply_leave'))
    print(rbac.has_permission('M456', 'approve_leave'))
    print(rbac.has_permission('E123', 'approve_leave'))
