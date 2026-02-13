"""
Audit Trail and Compliance Logging
Logs all leave actions with timestamp, user, action type, and restricts access by role.
"""

from typing import List, Dict
from datetime import datetime

class AuditEntry:
    def __init__(self, user_id: str, action: str, target_id: str, details: str):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.user_id = user_id
        self.action = action
        self.target_id = target_id
        self.details = details

class AuditLog:
    def __init__(self):
        self.entries: List[AuditEntry] = []
    def log(self, user_id: str, action: str, target_id: str, details: str):
        entry = AuditEntry(user_id, action, target_id, details)
        self.entries.append(entry)
        print(f"Audit: {entry.timestamp} | {user_id} | {action} | {target_id} | {details}")
    def get_entries(self, role: str, user_id: str = None) -> List[AuditEntry]:
        # Only HR/Admin or Auditor can see all logs; others see their own
        if role in ["hr_admin", "auditor"]:
            return self.entries
        else:
            return [e for e in self.entries if e.user_id == user_id]

# Example usage
if __name__ == "__main__":
    log = AuditLog()
    log.log("u123", "Create", "leave_1", "Applied for casual leave")
    log.log("m456", "Approve", "leave_1", "Approved by manager")
    print("All entries (HR):")
    for e in log.get_entries("hr_admin"):
        print(vars(e))
    print("Own entries (Employee):")
    for e in log.get_entries("employee", "u123"):
        print(vars(e))
