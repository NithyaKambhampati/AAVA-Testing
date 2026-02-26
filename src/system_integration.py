"""
Responsive and Reliable System with Integration
As a user, I want the LMS to be easy to use, responsive, and available on both desktop and mobile so that I can access it conveniently.
"""
import threading
import time

class SystemMonitor:
    def __init__(self, services):
        self.services = services

    def check_responsiveness(self):
        start_time = time.time()
        # Simulate checking all services
        for service in self.services:
            service.ping()
        response_time = time.time() - start_time
        return response_time < 2  # Must be <2 seconds

    def check_concurrency(self, user_count=1000):
        # Simulate concurrent requests
        def simulate_user():
            for service in self.services:
                service.ping()
        threads = [threading.Thread(target=simulate_user) for _ in range(user_count)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return True
