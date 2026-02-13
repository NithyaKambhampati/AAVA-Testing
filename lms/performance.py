"""
System Performance and Scalability
Simulates performance metrics collection and scaling hooks.
"""

import time
import random

class PerformanceMetrics:
    def __init__(self):
        self.response_times = []
        self.concurrent_users = 0
    def record_response(self, duration: float):
        self.response_times.append(duration)
    def average_response_time(self):
        if not self.response_times:
            return 0.0
        return sum(self.response_times) / len(self.response_times)
    def set_concurrent_users(self, count: int):
        self.concurrent_users = count
    def is_scaling_needed(self):
        # Example: scale if > 500 users or avg response > 2s
        return self.concurrent_users > 500 or self.average_response_time() > 2.0

# Example usage
if __name__ == "__main__":
    perf = PerformanceMetrics()
    for _ in range(600):
        t = random.uniform(1.0, 2.5)
        perf.record_response(t)
    perf.set_concurrent_users(600)
    print(f"Avg response: {perf.average_response_time():.2f}s, scaling needed: {perf.is_scaling_needed()}")
