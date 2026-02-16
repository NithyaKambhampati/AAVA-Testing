"""
HR/Admin Leave Reporting Module
- Allows HR/Admin to view leave reports for teams and organization
- Handles report generation failures
"""

class LeaveReportingError(Exception):
    pass

class LeaveReportingService:
    def __init__(self, report_client):
        self.report_client = report_client

    def generate_report(self, scope: str = "organization", filters: dict = None) -> dict:
        try:
            return self.report_client.fetch_leave_report(scope, filters or {})
        except Exception as e:
            raise LeaveReportingError(f"Report generation failed: {str(e)}")
