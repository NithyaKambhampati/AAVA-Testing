"""
Integration with Employee/HR Systems Module
- Syncs employee and leave data with HRIS
- Handles sync errors and logs
"""

import time
from typing import Dict

HRIS_DATA = {'alice@company.com': {'leave_balance': 10, 'department': 'HR'}}
LEAVE_BALANCES = {'alice@company.com': 5}
INTEGRATION_LOG = []


def sync_with_hris():
    try:
        for email, hris_info in HRIS_DATA.items():
            LEAVE_BALANCES[email] = hris_info['leave_balance']
        INTEGRATION_LOG.append({'timestamp': int(time.time()), 'status': 'SUCCESS'})
        return {'status': 'SYNCED', 'leave_balances': LEAVE_BALANCES}
    except Exception as e:
        INTEGRATION_LOG.append({'timestamp': int(time.time()), 'status': 'FAILED', 'error': str(e)})
        return {'status': 'FAILED', 'error': str(e)}

def check_integration_logs():
    return INTEGRATION_LOG

if __name__ == "__main__":
    print(sync_with_hris())
    print("Integration Logs:", check_integration_logs())
