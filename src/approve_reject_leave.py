"""
Approve or Reject Leave Requests
As a manager, I want to approve or reject leave requests with optional comments, so that employees are informed about decisions.
"""
class LeaveApprovalService:
    def approve(self, leave_request, comment=None):
        if leave_request['status'] != 'pending':
            return {'status': 'error', 'message': 'Leave request not pending'}
        if leave_request.get('balance', 1) == 0:
            return {'status': 'error', 'message': 'Cannot approve leave with zero balance'}
        leave_request['status'] = 'approved'
        leave_request['manager_comment'] = comment
        return {'status': 'success', 'request': leave_request, 'message': 'Leave approved'}

    def reject(self, leave_request, comment=None):
        if leave_request['status'] != 'pending':
            return {'status': 'error', 'message': 'Leave request not pending'}
        leave_request['status'] = 'rejected'
        leave_request['manager_comment'] = comment
        return {'status': 'success', 'request': leave_request, 'message': 'Leave rejected'}

# Example usage
if __name__ == '__main__':
    leave_request = {'employee_id': 'E123', 'manager_id': 'M456', 'type': 'casual', 'start': '2024-07-01', 'end': '2024-07-02', 'status': 'pending', 'balance': 2}
    approval_service = LeaveApprovalService()
    print(approval_service.approve(leave_request, 'Enjoy your vacation!'))
    leave_request['status'] = 'pending'
    print(approval_service.reject(leave_request, 'Business needs'))
