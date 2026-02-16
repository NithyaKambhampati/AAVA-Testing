"""
Audit Trail Maintenance Module
- Maintains immutable audit logs for all leave actions
- Detects and reports tampering attempts
"""

import hashlib
from datetime import datetime

class AuditTrailError(Exception):
    pass

class AuditTrailService:
    def __init__(self, audit_client):
        self.audit_client = audit_client
        self.last_hash = None

    def log_action(self, entity: str, entity_id: str, action: str, performed_by: str, details: dict) -> bool:
        timestamp = datetime.utcnow().isoformat()
        record = {
            'entity': entity,
            'entity_id': entity_id,
            'action': action,
            'performed_by': performed_by,
            'performed_at': timestamp,
            'details': details,
            'prev_hash': self.last_hash or ''
        }
        record_str = str(record)
        record_hash = hashlib.sha256(record_str.encode()).hexdigest()
        record['hash'] = record_hash
        self.last_hash = record_hash
        try:
            self.audit_client.append_log(record)
            return True
        except Exception as e:
            raise AuditTrailError(f"Failed to log audit action: {str(e)}")

    def detect_tampering(self, logs: list) -> bool:
        prev_hash = ''
        for log in logs:
            expected_hash = hashlib.sha256(str({k:log[k] for k in log if k != 'hash'}).encode()).hexdigest()
            if log['hash'] != expected_hash or log.get('prev_hash','') != prev_hash:
                # Alert security
                print(f"Tampering detected in audit log: {log}")
                return True
            prev_hash = log['hash']
        return False
