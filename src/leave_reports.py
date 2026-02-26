"""
HR/Admin Access to Leave Reports
As an HR/Admin, I want to view organization-wide leave reports so that I can monitor trends and ensure compliance.
"""

class LeaveReportService:
    def __init__(self, report_repo):
        self.report_repo = report_repo

    def get_organization_leave_report(self):
        return self.report_repo.get_aggregate_leave_data()

    def get_pending_approvals_report(self):
        return self.report_repo.get_pending_approvals()
