"""
System Reliability and Performance
User Story: As a user, I want the LMS to have minimal downtime and support concurrent users during peak periods so that my experience is uninterrupted.
Acceptance Criteria:
- Peak usage: response times <2 seconds, uptime >99.5%.
"""

import time
import random

class ReliabilityService:
    def __init__(self):
        self.uptime = 100.0  # Simulated uptime percentage

    def simulate_response_time(self, concurrent_users: int) -> float:
        # Simulate response time (ms) based on concurrent users
        base = 500  # ms
        extra = concurrent_users * 10  # ms per user
        response_time = base + extra
        return response_time / 1000.0  # seconds

    def check_uptime(self) -> float:
        # Simulate uptime check
        return self.uptime

# Example usage:
if __name__ == "__main__":
    svc = ReliabilityService()
    print("Response time (100 users):", svc.simulate_response_time(100), "seconds")
    print("System uptime:", svc.check_uptime(), "%")
