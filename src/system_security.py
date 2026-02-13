"""
System Security Module
- Enforces data protection and access control
- Reviews security logs and detects unauthorized access
"""

from typing import List, Dict

SECURITY_LOGS: List[Dict] = []


def log_security_event(user: str, action: str, result: str):
    SECURITY_LOGS.append({'user': user, 'action': action, 'result': result})

def review_security_logs() -> List[Dict]:
    return SECURITY_LOGS

def detect_unauthorized_access() -> bool:
    for log in SECURITY_LOGS:
        if log['result'] == 'UNAUTHORIZED':
            return True
    return False

if __name__ == "__main__":
    log_security_event('alice@company.com', 'login', 'AUTHORIZED')
    log_security_event('eve@company.com', 'access_admin', 'UNAUTHORIZED')
    print("Security Logs:", review_security_logs())
    print("Unauthorized Access Detected:", detect_unauthorized_access())
