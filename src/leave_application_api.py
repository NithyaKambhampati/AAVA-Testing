from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Mocked user leave balances (in a real system, this would be in a database)
user_leave_balances = {
 'employee1': {
 'annual': 10,
 'sick': 5,
 'casual': 3
 }
}

# Mocked leave requests storage
leave_requests = {}

# Helper function to validate leave dates
def validate_dates(start_date_str, end_date_str):
 try:
 start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
 end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
 if end_date < start_date:
 return False, 'End date cannot be earlier than start date.'
 return True, ''
 except ValueError:
 return False, 'Invalid date format. Use YYYY-MM-DD.'

# Helper function to check leave balance
def has_sufficient_balance(username, leave_type, days_requested):
 balance = user_leave_balances.get(username, {}).get(leave_type, 0)
 if balance >= days_requested:
 return True
 return False

@app.route('/api/v1/leave/apply', methods=['POST'])
def apply_leave():
 data = request.get_json()
 required_fields = ['username', 'leave_type', 'start_date', 'end_date']
 for field in required_fields:
 if field not in data:
 return jsonify({'error': f'Missing field: {field}'}), 400
 username = data['username']
 leave_type = data['leave_type']
 start_date = data['start_date']
 end_date = data['end_date']
 reason = data.get('reason', '')

 # Validate dates
 valid, msg = validate_dates(start_date, end_date)
 if not valid:
 return jsonify({'error': msg}), 400

 # Calculate number of leave days (inclusive)
 start_dt = datetime.strptime(start_date, '%Y-%m-%d')
 end_dt = datetime.strptime(end_date, '%Y-%m-%d')
 days_requested = (end_dt - start_dt).days + 1
 if days_requested <= 0:
 return jsonify({'error': 'Leave duration must be at least 1 day.'}), 400

 # Check leave type exists
 if leave_type not in user_leave_balances.get(username, {}):
 return jsonify({'error': 'Invalid leave type.'}), 400

 # Check leave balance
 if not has_sufficient_balance(username, leave_type, days_requested):
 return jsonify({'error': 'Insufficient leave balance.'}), 400

 # Create leave request
 request_id = str(uuid.uuid4())
 leave_requests[request_id] = {
 'username': username,
 'leave_type': leave_type,
 'start_date': start_date,
 'end_date': end_date,
 'reason': reason,
 'status': 'pending',
 'created_at': datetime.utcnow().isoformat()
 }
 return jsonify({'message': 'Leave request submitted successfully.', 'request_id': request_id}), 201

if __name__ == '__main__':
 app.run(debug=True)
