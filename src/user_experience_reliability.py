"""
Responsive User Experience and Reliability
User Story: As a user, I want the LMS to be easy to use, responsive, and reliable, so that I can manage leave from desktop or mobile with minimal downtime.
"""

import time
import random

def simulate_ui_response(action: str) -> str:
    """
    Simulates UI response time and reliability for a given action.
    Ensures response time <2s and uptime >99.5%.
    """
    # Simulate peak load
    response_time = random.uniform(0.2, 1.8)
    if random.random() < 0.005:  # 0.5% chance of downtime
        time.sleep(2.5)
        return f"Error: Service unavailable during '{action}'. Please try again later."
    time.sleep(response_time)
    return f"Action '{action}' completed in {response_time:.2f}s."

if __name__ == "__main__":
    actions = ['login', 'apply_leave', 'view_dashboard', 'approve_request']
    for action in actions:
        print(simulate_ui_response(action))
