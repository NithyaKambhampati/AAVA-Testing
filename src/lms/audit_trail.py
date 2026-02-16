"""
Comprehensive Audit Trail
User Story: As an HR/admin or auditor, I want the system to maintain audit logs of all leave-related actions with timestamps and user details so that compliance can be ensured.
Acceptance Criteria:
- All actions recorded with user, timestamp, and details; logs are traceable.
"""

from typing import List, Dict
from datetime import datetime

class AuditLogEntry:
    def __init__(self, action: str, user_id: str, leave_id: str, details: str):
        self.timestamp = datetime.now()
        self.action = action
        self.user_id = user_id
        self.leave_id = leave_id
        self.details = details

    def __repr__(self):
        return f"[{self.timestamp}] {self.action} by {self.user_id} on {self.leave_id}: {self.details}"

class AuditTrailService:
    def __init__(self):
        self.logs: List[AuditLogEntry] = []

    def log_action(self, action: str, user_id: str, leave_id: str, details: str):
        entry = AuditLogEntry(action, user_id, leave_id, details)
        self.logs.append(entry)

    def get_logs(self) -> List[AuditLogEntry]:
        return self.logs

# Example usage:
if __name__ == "__main__":
    svc = AuditTrailService()
    svc.log_action("create", "E123", "L1", "Applied for sick leave 2024-06-10 to 2024-06-12")
    svc.log_action("approve", "M456", "L1", "Approved with comment: Get well soon!")
    for log in svc.get_logs():
        print(log)
