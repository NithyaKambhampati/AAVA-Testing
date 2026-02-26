"""
Complete Audit Trail of Leave Actions
As an HR/Admin, I want the system to keep a complete, immutable audit trail of all leave actions so that compliance and traceability are ensured.
"""
from datetime import datetime

class AuditTrailService:
    def __init__(self, audit_repo):
        self.audit_repo = audit_repo

    def record_action(self, entity: str, entity_id: int, action: str, actor_id: int, details: dict):
        log_entry = {
            'entity': entity,
            'entity_id': entity_id,
            'action': action,
            'actor_id': actor_id,
            'timestamp': datetime.utcnow().isoformat(),
            'details': details
        }
        self.audit_repo.append(log_entry)
        # Audit logs must not be editable
        return True
