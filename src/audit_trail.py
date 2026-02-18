# audit_trail.py

from datetime import datetime
from typing import List, Dict

class AuditTrail:
    def __init__(self):
        self.logs = []

    def log_action(self, user_id: str, action: str, entity: str, entity_id: int, before_state: Dict, after_state: Dict):
        log_entry = {
            "user_id": user_id,
            "action": action,
            "entity": entity,
            "entity_id": entity_id,
            "before_state": before_state,
            "after_state": after_state,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.logs.append(log_entry)

    def get_logs_for_entity(self, entity: str, entity_id: int) -> List[Dict]:
        return [log for log in self.logs if log['entity'] == entity and log['entity_id'] == entity_id]

    def get_all_logs(self) -> List[Dict]:
        return self.logs

# Example usage
if __name__ == "__main__":
    audit = AuditTrail()
    before = {"status": "pending"}
    after = {"status": "approved"}
    audit.log_action("mgr001", "approve", "leave_request", 1, before, after)
    print(audit.get_logs_for_entity("leave_request", 1))
    print(audit.get_all_logs())
