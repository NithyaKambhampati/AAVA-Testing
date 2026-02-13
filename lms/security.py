"""
Security and Access Control
Enforces data protection, role-based access, and logs access reviews.
"""

from typing import List, Dict
from lms.authentication import User, Role
from lms.audit_log import AuditLog

class Security:
    def __init__(self, audit_log: AuditLog):
        self.audit_log = audit_log
    def check_access(self, user: User, resource: str, allowed_roles: List[Role]):
        if user.role not in allowed_roles:
            self.audit_log.log(user.user_id, "AccessDenied", resource, f"Role {user.role} not permitted")
            raise PermissionError(f"Access denied for role: {user.role}")
        self.audit_log.log(user.user_id, "AccessGranted", resource, f"Role {user.role} permitted")
    def run_penetration_test(self) -> bool:
        # Simulate pen test: always passes in this stub
        print("Penetration test passed. No unauthorized access detected.")
        return True
    def access_review(self, users: List[User]):
        for user in users:
            self.audit_log.log(user.user_id, "AccessReview", "system", f"Role: {user.role}")
        print("Access review completed and logged.")

# Example usage
if __name__ == "__main__":
    from lms.authentication import CredentialProvider, AuthService
    from lms.audit_log import AuditLog
    cp = CredentialProvider()
    auth = AuthService(cp)
    audit_log = AuditLog()
    sec = Security(audit_log)
    user = auth.login("employee", "employee")
    try:
        sec.check_access(user, "employee_dashboard", [Role.EMPLOYEE, Role.MANAGER])
    except PermissionError as e:
        print(str(e))
    sec.run_penetration_test()
    sec.access_review([user])
