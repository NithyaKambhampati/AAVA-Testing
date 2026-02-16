"""
System Integration with HR/Employee Systems Module
- Syncs leave balances and user data with HRIS
- Handles integration failures and alerts admin
"""

class IntegrationError(Exception):
    pass

class HRIntegrationService:
    def __init__(self, hris_client):
        self.hris_client = hris_client

    def sync_user_data(self, user_id: str) -> bool:
        try:
            self.hris_client.sync_user(user_id)
            return True
        except Exception as e:
            self.alert_admin(f"User data sync failed for {user_id}: {e}")
            raise IntegrationError(f"User data sync failed: {str(e)}")

    def sync_leave_balances(self, user_id: str) -> bool:
        try:
            self.hris_client.sync_leave_balance(user_id)
            return True
        except Exception as e:
            self.alert_admin(f"Leave balance sync failed for {user_id}: {e}")
            raise IntegrationError(f"Leave balance sync failed: {str(e)}")

    def alert_admin(self, message: str):
        # Placeholder for alerting admin (e.g., email, dashboard)
        print(f"ADMIN ALERT: {message}")
