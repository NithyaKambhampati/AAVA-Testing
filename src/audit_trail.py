"""
Audit Trail for Leave Actions
As the system, I want to maintain a complete audit trail of all leave-related actions, so that compliance and traceability are ensured.
"""
from datetime import datetime

class AuditTrail:
    def __init__(self):
        self.logs = []

    def record(self, entity, entity_id, action, user_id, details=None):
        entry = {
            'entity': entity,
            'entity_id': entity_id,
            'action': action,
            'user_id': user_id,
            'timestamp': datetime.now().isoformat(),
            'details': details
        }
        self.logs.append(entry)
        return entry

    def get_logs(self):
        return self.logs

# Example usage
if __name__ == '__main__':
    audit = AuditTrail()
    audit.record('leave_request', 'LR123', 'create', 'E123', {'dates': '2024-07-01 to 2024-07-02'})
    audit.record('leave_request', 'LR123', 'approve', 'M456', {'comment': 'Enjoy your leave'})
    print(audit.get_logs())
