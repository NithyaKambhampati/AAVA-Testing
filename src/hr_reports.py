"""
HR/Admin Views Organization and Team Leave Reports
As an HR/admin user, I want to view leave reports across teams and the organization so that I can monitor trends and compliance.
"""

from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Mocked leave data
LEAVE_REQUESTS = [
    {"username": "employee1", "leaveType": "casual", "startDate": "2024-07-01", "endDate": "2024-07-03", "status": "Approved", "team": "TeamA"},
    {"username": "employee2", "leaveType": "sick", "startDate": "2024-06-10", "endDate": "2024-06-12", "status": "Pending", "team": "TeamA"}
]

@app.route('/leave-reports', methods=['GET'])
def leave_reports():
    role = session.get('role')
    if role != 'hradmin':
        return jsonify({"error": "Not authorized"}), 403
    team = request.args.get('team')
    leave_type = request.args.get('type')
    period = request.args.get('period')  # e.g., '2024-06'
    filtered = LEAVE_REQUESTS
    if team:
        filtered = [r for r in filtered if r['team'] == team]
    if leave_type:
        filtered = [r for r in filtered if r['leaveType'] == leave_type]
    if period:
        filtered = [r for r in filtered if r['startDate'].startswith(period)]
    return jsonify({"report": filtered}), 200

if __name__ == '__main__':
    app.run(debug=True)
