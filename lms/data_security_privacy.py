"""
Data Security and Privacy Enforcement Module
- Enforces data security and privacy policies
- Logs unauthorized access attempts and alerts admin on breaches
"""

class SecurityBreachError(Exception):
    pass

class DataSecurityService:
    def __init__(self, security_client, audit_service):
        self.security_client = security_client
        self.audit_service = audit_service

    def enforce_access(self, user_id: str, resource: str, action: str) -> bool:
        if not self.security_client.is_authorized(user_id, resource, action):
            self.audit_service.log_action(
                entity=resource,
                entity_id=user_id,
                action="UNAUTHORIZED_ACCESS",
                performed_by=user_id,
                details={"attempted_action": action}
            )
            raise SecurityBreachError(f"Unauthorized access attempt by {user_id} on {resource}:{action}")
        return True

    def handle_security_breach(self, user_id: str, details: dict):
        # Placeholder for alerting admin/security team
        print(f"SECURITY ALERT: Breach attempt by {user_id}. Details: {details}")
        self.audit_service.log_action(
            entity="SECURITY",
            entity_id=user_id,
            action="SECURITY_BREACH",
            performed_by=user_id,
            details=details
        )
