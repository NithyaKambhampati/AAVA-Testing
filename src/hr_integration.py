# hr_integration.py

from typing import Dict, Any
from datetime import datetime

class HRIntegrationAdapter:
    def __init__(self):
        self.sync_log = []
        self.hr_data = {}

    def sync_employee_data(self, employee_data: Dict[str, Any]):
        # Simulate data sync
        self.hr_data.update(employee_data)
        self._log_sync('employee_data', employee_data)
        return {"message": "Employee data synchronized"}

    def sync_leave_balances(self, balances: Dict[str, int]):
        self.hr_data['leave_balances'] = balances
        self._log_sync('leave_balances', balances)
        return {"message": "Leave balances synchronized"}

    def _log_sync(self, sync_type: str, data: Any):
        self.sync_log.append({
            "sync_type": sync_type,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_sync_log(self):
        return self.sync_log

# Example usage
if __name__ == "__main__":
    adapter = HRIntegrationAdapter()
    print(adapter.sync_employee_data({'emp001': {'name': 'John Doe', 'role': 'employee'}}))
    print(adapter.sync_leave_balances({'sick': 5, 'casual': 7}))
    print(adapter.get_sync_log())
