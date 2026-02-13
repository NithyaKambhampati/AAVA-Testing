"""
Integration with HR/Employee Systems
Synchronizes leave and user data with external HR systems. Implements retry and error logging.
"""

from typing import Dict
from datetime import datetime

class IntegrationError(Exception):
    pass

class IntegrationLog:
    def __init__(self):
        self.entries = []
    def log(self, event: str, status: str, details: str):
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "event": event,
            "status": status,
            "details": details
        }
        self.entries.append(entry)
        print(f"Integration log: {entry}")

class HRIntegration:
    def __init__(self, log: IntegrationLog):
        self.log = log
    def sync_leave(self, employee_id: str, leave_data: Dict, retry: int = 3):
        for attempt in range(retry):
            try:
                # Replace with actual API call to HR system
                # Simulate 99% success
                import random
                if random.random() < 0.99:
                    self.log.log("leave_sync", "success", f"Employee {employee_id}: {leave_data}")
                    return True
                else:
                    raise IntegrationError("Simulated integration failure")
            except Exception as e:
                self.log.log("leave_sync", "failure", str(e))
        return False

# Example usage
if __name__ == "__main__":
    log = IntegrationLog()
    integ = HRIntegration(log)
    integ.sync_leave("u123", {"type": "casual", "days": 2, "status": "Approved"})
