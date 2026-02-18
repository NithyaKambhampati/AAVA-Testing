# reporting.py

from typing import List, Dict
from datetime import datetime

class LeaveReporting:
    def __init__(self, leave_history: List[Dict]):
        self.leave_history = leave_history

    def generate_report(self, filter_type: str = None, filter_status: str = None):
        filtered = self.leave_history
        if filter_type:
            filtered = [req for req in filtered if req['type'] == filter_type]
        if filter_status:
            filtered = [req for req in filtered if req['status'] == filter_status]
        return filtered

    def leave_trends(self):
        trends = {}
        for req in self.leave_history:
            key = req['type']
            if key not in trends:
                trends[key] = 0
            trends[key] += 1
        return trends

    def export_to_csv(self):
        import csv
        from io import StringIO
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=['id', 'user_id', 'type', 'start', 'end', 'status'])
        writer.writeheader()
        for req in self.leave_history:
            writer.writerow(req)
        return output.getvalue()

# Example usage
if __name__ == "__main__":
    history = [
        {"id": 1, "user_id": "emp001", "type": "casual", "start": "2024-06-10", "end": "2024-06-12", "status": "approved"},
        {"id": 2, "user_id": "emp002", "type": "sick", "start": "2024-06-13", "end": "2024-06-14", "status": "rejected"},
        {"id": 3, "user_id": "emp003", "type": "casual", "start": "2024-06-17", "end": "2024-06-18", "status": "pending"}
    ]
    reporting = LeaveReporting(history)
    print(reporting.generate_report(filter_type='casual'))
    print(reporting.leave_trends())
    print(reporting.export_to_csv())
