"""
Role-Based Access Control (RBAC) Module
- Enforces access restrictions based on user roles
- Updates permissions on role change
"""

class AccessDeniedError(Exception):
    pass

class RBACService:
    def __init__(self, rbac_client):
        self.rbac_client = rbac_client

    def check_access(self, user_id: str, resource: str, action: str) -> bool:
        permissions = self.rbac_client.get_permissions(user_id)
        if (resource, action) not in permissions:
            raise AccessDeniedError(f"Access denied for {user_id} on {resource}:{action}")
        return True

    def update_role(self, user_id: str, new_role: str) -> bool:
        try:
            self.rbac_client.update_user_role(user_id, new_role)
            return True
        except Exception as e:
            raise AccessDeniedError(f"Role update failed: {str(e)}")
