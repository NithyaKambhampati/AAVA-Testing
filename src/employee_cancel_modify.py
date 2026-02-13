"""
Employee Cancels or Modifies Leave Request
As an employee, I want to cancel or modify my leave requests before approval so that I can adjust my plans if needed.
"""

from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Mocked leave requests
LEAVE_REQUESTS = [
    {"id": 1, "username": "employee1", "leaveType": "casual", "startDate": "2024-07-01", "endDate": "2024-07-03", "reason": "Vacation", "status": "Pending"}
]

@app.route('/cancel-leave', methods=['POST'])
def cancel_leave():
    username = session.get('username')
    if not username:
        return jsonify({"error": "Not authenticated"}), 401
    data = request.json
    leave_id = data.get('leaveId')
    for req in LEAVE_REQUESTS:
        if req['id'] == leave_id and req['username'] == username and req['status'] == 'Pending':
            req['status'] = 'Cancelled'
            return jsonify({"message": "Leave request cancelled", "request": req}), 200
    return jsonify({"error": "Leave request not found or not cancellable."}), 404

@app.route('/modify-leave', methods=['POST'])
def modify_leave():
    username = session.get('username')
    if not username:
        return jsonify({"error": "Not authenticated"}), 401
    data = request.json
    leave_id = data.get('leaveId')
    new_start = data.get('startDate')
    new_end = data.get('endDate')
    new_reason = data.get('reason', '')
    for req in LEAVE_REQUESTS:
        if req['id'] == leave_id and req['username'] == username and req['status'] == 'Pending':
            req['startDate'] = new_start
            req['endDate'] = new_end
            req['reason'] = new_reason
            return jsonify({"message": "Leave request modified", "request": req}), 200
    return jsonify({"error": "Leave request not found or not modifiable."}), 404

if __name__ == '__main__':
    app.run(debug=True)
