# Leave Application API (Flask Example)
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Simulated in-memory data stores
USERS = {
 'emp001': {'name': 'Alice', 'leave_balance': {'annual': 10, 'sick': 5}},
 'emp002': {'name': 'Bob', 'leave_balance': {'annual': 8, 'sick': 2}},
}
LEAVE_REQUESTS = []

@app.route('/api/v1/leave/apply', methods=['POST'])
def apply_leave():
 data = request.get_json()
 required_fields = ['employee_id', 'leave_type', 'start_date', 'end_date']
 for field in required_fields:
 if field not in data:
 return jsonify({'error': f'Missing field: {field}'}), 400
 employee_id = data['employee_id']
 leave_type = data['leave_type']
 start_date = data['start_date']
 end_date = data['end_date']
 reason = data.get('reason', '')

 # Validate user
 if employee_id not in USERS:
 return jsonify({'error': 'Invalid employee ID'}), 404
 # Validate leave type
 if leave_type not in USERS[employee_id]['leave_balance']:
 return jsonify({'error': 'Invalid leave type'}), 400
 # Validate dates
 try:
 start_dt = datetime.strptime(start_date, '%Y-%m-%d')
 end_dt = datetime.strptime(end_date, '%Y-%m-%d')
 except ValueError:
 return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400
 if end_dt < start_dt:
 return jsonify({'error': 'End date cannot be earlier than start date.'}), 400
 days_requested = (end_dt - start_dt).days + 1
 # Check leave balance
 balance = USERS[employee_id]['leave_balance'][leave_type]
 if balance < days_requested:
 return jsonify({'error': 'Insufficient leave balance.'}), 400
 # (Optional) Check for overlapping requests
 for req in LEAVE_REQUESTS:
 if req['employee_id'] == employee_id and req['leave_type'] == leave_type:
 existing_start = datetime.strptime(req['start_date'], '%Y-%m-%d')
 existing_end = datetime.strptime(req['end_date'], '%Y-%m-%d')
 if (start_dt <= existing_end and end_dt >= existing_start):
 return jsonify({'error': 'Overlapping leave request exists.'}), 400
 # All validations passed, create leave request
 request_id = str(uuid.uuid4())
 leave_req = {
 'request_id': request_id,
 'employee_id': employee_id,
 'leave_type': leave_type,
 'start_date': start_date,
 'end_date': end_date,
 'reason': reason,
 'status': 'Pending',
 'created_at': datetime.utcnow().isoformat() + 'Z'
 }
 LEAVE_REQUESTS.append(leave_req)
 return jsonify({'message': 'Leave request submitted successfully.', 'request_id': request_id}), 201

# For testing: get all leave requests
@app.route('/api/v1/leave/requests', methods=['GET'])
def get_requests():
 return jsonify(LEAVE_REQUESTS)

if __name__ == '__main__':
 app.run(debug=True)
