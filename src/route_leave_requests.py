"""
Route Leave Requests for Approval
As the system, I want to route submitted leave requests to the employee’s reporting manager, so that approvals are handled efficiently.
"""
class LeaveRoutingService:
    def __init__(self, org_structure):
        self.org_structure = org_structure

    def route_to_manager(self, employee_id, leave_request):
        manager_id = self.org_structure.get(employee_id)
        if not manager_id:
            return {'status': 'error', 'message': 'Manager not assigned'}
        # Simulate routing
        leave_request['status'] = 'pending'
        leave_request['manager_id'] = manager_id
        return {'status': 'success', 'request': leave_request, 'message': 'Leave request routed to manager'}

# Example usage
if __name__ == '__main__':
    org_structure = {'E123': 'M456'}
    leave_request = {'type': 'casual', 'start': '2024-07-01', 'end': '2024-07-02', 'status': 'draft'}
    routing_service = LeaveRoutingService(org_structure)
    result = routing_service.route_to_manager('E123', leave_request)
    print(result)
