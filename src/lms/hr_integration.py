"""
Integration with HR and Credential Systems
User Story: As the LMS, I want to integrate with existing employee/HR systems and organizational credentials so that user data and authentication are seamless.
Acceptance Criteria:
- HR system changes reflected in LMS in near real-time; valid credentials grant seamless access.
"""

# Stub for HR/credential integration. In practice, would use REST API, SSO, etc.

class HRIntegrationService:
    def __init__(self, hr_api):
        self.hr_api = hr_api  # Simulated HR API (dict)

    def sync_user_data(self, employee_id: str) -> dict:
        # Simulate pulling user data from HR system
        return self.hr_api.get(employee_id, {})

    def authenticate(self, username: str, password: str) -> bool:
        # Simulate credential check
        user = self.hr_api.get(username)
        return user and user.get("password") == password

# Example usage:
if __name__ == "__main__":
    hr_api = {
        "E123": {"name": "Alice", "role": "employee", "password": "alicepw"},
        "E124": {"name": "Bob", "role": "manager", "password": "bobpw"}
    }
    svc = HRIntegrationService(hr_api)
    print(svc.sync_user_data("E123"))
    print(svc.authenticate("E123", "alicepw"))
    print(svc.authenticate("E123", "wrongpw"))
