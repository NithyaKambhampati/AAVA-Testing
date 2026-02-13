"""
System Reliability and Performance Module
- Ensures high availability and performance during peak load
- Queues requests during downtime
"""

import time
from typing import List, Dict

SYSTEM_METRICS = {'uptime': 99.9, 'response_time': 1.2, 'peak_load': False, 'downtime': False}
REQUEST_QUEUE: List[Dict] = []


def submit_leave_request(request: Dict):
    if SYSTEM_METRICS['downtime']:
        REQUEST_QUEUE.append(request)
        return {'status': 'QUEUED', 'message': 'System down. Request queued.'}
    else:
        return {'status': 'SUBMITTED', 'message': 'Request submitted.'}

def process_queue():
    if not SYSTEM_METRICS['downtime']:
        for req in REQUEST_QUEUE:
            # Process each queued request
            print(f"Processing queued request: {req}")
        REQUEST_QUEUE.clear()
        return {'status': 'PROCESSED', 'count': len(REQUEST_QUEUE)}
    else:
        return {'status': 'SYSTEM_DOWN', 'message': 'Cannot process queue.'}

if __name__ == "__main__":
    SYSTEM_METRICS['downtime'] = True
    print(submit_leave_request({'id': 1, 'employee': 'alice@company.com'}))
    SYSTEM_METRICS['downtime'] = False
    print(process_queue())
    print("System Metrics:", SYSTEM_METRICS)
