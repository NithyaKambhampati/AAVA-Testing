from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock user leave balances (in a real system, fetch from DB)
USER_LEAVE_BALANCES = {
    'employee1': {
        'annual': 10,
        'sick': 5,
        'casual': 3
    }
}

# Supported leave types
LEAVE_TYPES = {'annual', 'sick', 'casual'}

@app.route('/api/v1/leave/apply', methods=['POST'])
def apply_leave():
    data = request.get_json()
    required_fields = ['employee_id', 'start_date', 'end_date', 'leave_type', 'days']
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({'error': f'Missing fields: {", ".join(missing)}'}), 400

    employee_id = data['employee_id']
    start_date = data['start_date']
    end_date = data['end_date']
    leave_type = data['leave_type']
    days = data['days']

    # Validate leave type
    if leave_type not in LEAVE_TYPES:
        return jsonify({'error': 'Invalid leave type.'}), 400

    # Validate date format and order
    try:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    except Exception:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400
    if end_dt < start_dt:
        return jsonify({'error': 'End date cannot be earlier than start date.'}), 400

    # Validate leave balance
    user_balances = USER_LEAVE_BALANCES.get(employee_id)
    if not user_balances or leave_type not in user_balances:
        return jsonify({'error': 'Leave balance not found for user or leave type.'}), 400
    if user_balances[leave_type] < days:
        return jsonify({'error': 'Insufficient leave balance.'}), 400

    # Mock: Deduct leave (in real system, update DB)
    USER_LEAVE_BALANCES[employee_id][leave_type] -= days

    # Generate request ID
    request_id = str(uuid.uuid4())
    # Mock: Save leave request (in real system, persist to DB)

    return jsonify({
        'message': 'Leave request submitted successfully.',
        'request_id': request_id
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
