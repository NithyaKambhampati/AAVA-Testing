"""
Manager Approves/Rejects Leave Requests
As a manager, I want to approve or reject leave requests and add comments so that employees are informed of decisions and leave balances are updated appropriately.
"""

from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Mocked leave requests
LEAVE_REQUESTS = [
    {"id": 1, "username": "employee1", "leaveType": "casual", "startDate": "2024-07-01", "endDate": "2024-07-03", "reason": "Vacation", "status": "Pending", "manager": "manager1", "comment": ""}
]

@app.route('/approve-leave', methods=['POST'])
def approve_leave():
    username = session.get('username')
    role = session.get('role')
    if not username or role != 'manager':
        return jsonify({"error": "Not authorized"}), 403
    data = request.json
    leave_id = data.get('leaveId')
    comment = data.get('comment', '')
    for req in LEAVE_REQUESTS:
        if req['id'] == leave_id and req['manager'] == username and req['status'] == 'Pending':
            req['status'] = 'Approved'
            req['comment'] = comment
            # (In real system: update leave balance, notify employee)
            return jsonify({"message": "Leave approved", "request": req}), 200
    return jsonify({"error": "Leave request not found or already processed."}), 404

@app.route('/reject-leave', methods=['POST'])
def reject_leave():
    username = session.get('username')
    role = session.get('role')
    if not username or role != 'manager':
        return jsonify({"error": "Not authorized"}), 403
    data = request.json
    leave_id = data.get('leaveId')
    comment = data.get('comment', '')
    for req in LEAVE_REQUESTS:
        if req['id'] == leave_id and req['manager'] == username and req['status'] == 'Pending':
            req['status'] = 'Rejected'
            req['comment'] = comment
            return jsonify({"message": "Leave rejected", "request": req}), 200
    return jsonify({"error": "Leave request not found or already processed."}), 404

if __name__ == '__main__':
    app.run(debug=True)
