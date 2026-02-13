"""
Update Leave Balances
As the system, I want to update leave balances only after approval, so that balances remain accurate.
"""
def update_leave_balance(employee, leave_type, days, action):
    if action == 'approved':
        if employee.leave_balances.get(leave_type, 0) >= days:
            employee.leave_balances[leave_type] -= days
            return {'status': 'success', 'message': 'Leave balance updated', 'balance': employee.leave_balances[leave_type]}
        else:
            return {'status': 'error', 'message': 'Insufficient balance'}
    elif action in ['rejected', 'cancelled']:
        return {'status': 'success', 'message': 'No balance change'}
    else:
        return {'status': 'error', 'message': 'Invalid action'}

# Example usage
if __name__ == '__main__':
    from view_personal_details import Employee
    leave_balances = {'casual': 8, 'sick': 5, 'earned': 12}
    leave_history = []
    emp = Employee('E123', 'John Doe', leave_balances, leave_history)
    print(update_leave_balance(emp, 'casual', 2, 'approved'))
    print(update_leave_balance(emp, 'casual', 2, 'rejected'))
