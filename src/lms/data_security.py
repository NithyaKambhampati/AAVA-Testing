"""
Data Security and Protection
User Story: As the organization, I want all user and leave data to be protected with secure authentication and access control so that privacy and compliance are ensured.
Acceptance Criteria:
- Only authorized users can access/modify data; data encrypted as per standards.
"""

import hashlib

class DataSecurityService:
    def __init__(self, authorized_users):
        self.authorized_users = authorized_users  # set of user_ids

    def check_authorization(self, user_id: str) -> bool:
        return user_id in self.authorized_users

    def encrypt_data(self, data: str) -> str:
        # Simulate encryption (hashing for demo)
        return hashlib.sha256(data.encode()).hexdigest()

# Example usage:
if __name__ == "__main__":
    users = {"E123", "M456", "HR789"}
    svc = DataSecurityService(users)
    print(svc.check_authorization("E123"))  # True
    print(svc.check_authorization("X999"))  # False
    print(svc.encrypt_data("Sensitive leave request"))
