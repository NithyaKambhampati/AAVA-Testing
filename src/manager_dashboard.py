"""
Leave Request Routing and Manager Dashboard
As a manager, I want to view all pending leave requests from my team with relevant details so that I can review and take action efficiently.
"""

from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Mocked leave requests and manager assignments
LEAVE_REQUESTS = [
    {"username": "employee1", "leaveType": "casual", "startDate": "2024-07-01", "endDate": "2024-07-03", "reason": "Vacation", "status": "Pending", "manager": "manager1"}
]
TEAM_MEMBERS = {
    "manager1": ["employee1"]
}

@app.route('/manager-dashboard', methods=['GET'])
def manager_dashboard():
    username = session.get('username')
    role = session.get('role')
    if not username or role != 'manager':
        return jsonify({"error": "Not authorized"}), 403
    team = TEAM_MEMBERS.get(username, [])
    pending_requests = [req for req in LEAVE_REQUESTS if req['manager'] == username and req['status'] == 'Pending']
    return jsonify({"pendingRequests": pending_requests}), 200

if __name__ == '__main__':
    app.run(debug=True)
