# authentication.py

import hashlib
from typing import Dict

class AuthenticationService:
    def __init__(self, user_db: Dict[str, str]):
        """
        user_db: dict mapping username to hashed password (simulate org credentials)
        """
        self.user_db = user_db
        self.audit_log = []

    def login(self, username: str, password: str) -> bool:
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        if username in self.user_db and self.user_db[username] == hashed_pw:
            self._log_action(username, 'login_success')
            return True
        else:
            self._log_action(username, 'login_failure')
            return False

    def _log_action(self, username: str, action: str):
        from datetime import datetime
        self.audit_log.append({
            'user': username,
            'action': action,
            'timestamp': datetime.utcnow().isoformat()
        })

    def get_audit_log(self):
        return self.audit_log

# Example usage
if __name__ == "__main__":
    # Simulate org credentials
    users = {
        'alice': hashlib.sha256('password123'.encode()).hexdigest(),
        'bob': hashlib.sha256('securepass'.encode()).hexdigest()
    }
    auth = AuthenticationService(users)
    assert auth.login('alice', 'password123') == True
    assert auth.login('bob', 'wrongpass') == False
    print(auth.get_audit_log())
