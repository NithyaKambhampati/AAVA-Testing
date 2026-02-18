"""
Accessibility and Usability
As any user, I want to access the LMS from desktop and mobile devices so that I can manage leave anywhere, anytime.
"""

import time
import random

def is_desktop_accessible() -> bool:
    # Simulate desktop access check
    return True

def is_mobile_accessible() -> bool:
    # Simulate mobile access check
    return True

def check_performance():
    # Simulate peak load performance check
    start = time.time()
    user_count = random.randint(100, 500)
    for _ in range(user_count):
        time.sleep(0.001)  # Simulate user action
    elapsed = time.time() - start
    print(f"Handled {user_count} users in {elapsed:.2f} seconds.")
    return elapsed < 2.0

# Example usage
if __name__ == '__main__':
    print('Desktop accessible:', is_desktop_accessible())
    print('Mobile accessible:', is_mobile_accessible())
    performance_ok = check_performance()
    print('Performance within limits:', performance_ok)
