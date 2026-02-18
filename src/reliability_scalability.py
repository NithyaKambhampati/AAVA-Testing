# reliability_scalability.py

from datetime import datetime

class ReliabilityMonitor:
    def __init__(self):
        self.metrics = {
            'uptime': 99.9,
            'response_time': 1.5,
            'concurrent_users': 0
        }
        self.downtime_log = []

    def record_peak_usage(self, users: int):
        self.metrics['concurrent_users'] = users
        return f"Recorded {users} concurrent users."

    def record_downtime(self, start: str, end: str, reason: str):
        entry = {
            'start': start,
            'end': end,
            'reason': reason,
            'timestamp': datetime.utcnow().isoformat()
        }
        self.downtime_log.append(entry)
        return entry

    def get_metrics(self):
        return self.metrics

    def get_downtime_log(self):
        return self.downtime_log

# Example usage
if __name__ == "__main__":
    monitor = ReliabilityMonitor()
    print(monitor.record_peak_usage(1200))
    print(monitor.record_downtime('2024-06-15T02:00:00', '2024-06-15T03:00:00', 'Scheduled maintenance'))
    print(monitor.get_metrics())
    print(monitor.get_downtime_log())
