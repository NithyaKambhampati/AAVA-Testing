"""
Employee Applies for Leave
As an employee, I want to apply for various types of leave with selected dates and reasons so that my requests can be processed efficiently.
"""

from flask import Flask, request, jsonify, session
from datetime import datetime

app = Flask(__name__)

# Mocked leave balances and request storage
LEAVE_BALANCES = {
    "employee1": {"casual": 10, "sick": 5, "earned": 15},
}
LEAVE_REQUESTS = []

@app.route('/apply-leave', methods=['POST'])
def apply_leave():
    username = session.get('username')
    if not username:
        return jsonify({"error": "Not authenticated"}), 401
    data = request.json
    leave_type = data.get('leaveType')
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    reason = data.get('reason', '')

    # Validate dates
    try:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
        if end_dt < start_dt:
            return jsonify({"error": "End date cannot be before start date."}), 400
    except Exception:
        return jsonify({"error": "Invalid date format."}), 400

    # Validate balance
    balances = LEAVE_BALANCES.get(username, {})
    days_requested = (end_dt - start_dt).days + 1
    if balances.get(leave_type, 0) < days_requested:
        return jsonify({"error": "Insufficient leave balance."}), 400

    # Check overlapping requests
    for req in LEAVE_REQUESTS:
        if req['username'] == username and req['status'] in ['Pending', 'Approved']:
            req_start = datetime.strptime(req['startDate'], '%Y-%m-%d')
            req_end = datetime.strptime(req['endDate'], '%Y-%m-%d')
            if not (end_dt < req_start or start_dt > req_end):
                return jsonify({"error": "Overlapping leave request exists."}), 400

    # Create leave request
    new_request = {
        "username": username,
        "leaveType": leave_type,
        "startDate": start_date,
        "endDate": end_date,
        "reason": reason,
        "status": "Pending"
    }
    LEAVE_REQUESTS.append(new_request)
    return jsonify({"message": "Leave request submitted.", "request": new_request}), 201

if __name__ == '__main__':
    app.run(debug=True)
