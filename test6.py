from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mocked in-memory user leave balances (for demonstration)
user_leave_balances = {
    'employee1': {
        'casual': 5,
        'sick': 3,
        'earned': 10
    }
}

# Mocked in-memory leave requests
leave_requests = []

# Helper function to validate date format
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None

@app.route('/api/v1/leave/apply', methods=['POST'])
def apply_leave():
    data = request.get_json()
    required_fields = ['employee_id', 'leave_type', 'start_date', 'end_date']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    employee_id = data['employee_id']
    leave_type = data['leave_type']
    start_date_str = data['start_date']
    end_date_str = data['end_date']
    reason = data.get('reason', '')

    # Validate dates
    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)
    if not start_date or not end_date:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400
    if end_date < start_date:
        return jsonify({'error': 'End date cannot be earlier than start date.'}), 400

    # Validate leave type and balance
    balances = user_leave_balances.get(employee_id)
    if not balances or leave_type not in balances:
        return jsonify({'error': 'Invalid employee or leave type.'}), 400
    days_requested = (end_date - start_date).days + 1
    if balances[leave_type] < days_requested:
        return jsonify({'error': 'Insufficient leave balance.'}), 400

    # (Optional) Overlapping leave check (not implemented in this demo)

    # Create leave request
    request_id = len(leave_requests) + 1
    leave_request = {
        'request_id': request_id,
        'employee_id': employee_id,
        'leave_type': leave_type,
        'start_date': start_date_str,
        'end_date': end_date_str,
        'reason': reason,
        'status': 'Pending',
        'created_at': datetime.utcnow().isoformat() + 'Z'
    }
    leave_requests.append(leave_request)

    # For demo, deduct balance immediately (in real system, only after approval)
    # balances[leave_type] -= days_requested

    return jsonify({
        'message': 'Leave request submitted successfully.',
        'request_id': request_id
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
