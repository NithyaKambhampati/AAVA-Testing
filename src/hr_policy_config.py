"""
HR/Admin Configures Leave Types, Policies, and Calendars
As an HR/admin user, I want to configure leave types, policies, accrual rules, and holiday calendars so that the system reflects organizational rules.
"""

from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Mocked configuration
LEAVE_TYPES = ["casual", "sick", "earned"]
LEAVE_POLICIES = {"casual": {"max": 10}, "sick": {"max": 5}, "earned": {"max": 15}}
HOLIDAY_CALENDAR = ["2024-12-25", "2024-01-01"]

@app.route('/configure-leave-type', methods=['POST'])
def configure_leave_type():
    role = session.get('role')
    if role != 'hradmin':
        return jsonify({"error": "Not authorized"}), 403
    data = request.json
    leave_type = data.get('leaveType')
    max_days = data.get('maxDays')
    if leave_type and max_days:
        LEAVE_TYPES.append(leave_type)
        LEAVE_POLICIES[leave_type] = {"max": max_days}
        return jsonify({"message": "Leave type configured", "types": LEAVE_TYPES}), 201
    return jsonify({"error": "Invalid input"}), 400

@app.route('/update-holiday-calendar', methods=['POST'])
def update_holiday_calendar():
    role = session.get('role')
    if role != 'hradmin':
        return jsonify({"error": "Not authorized"}), 403
    data = request.json
    date = data.get('date')
    if date:
        HOLIDAY_CALENDAR.append(date)
        return jsonify({"message": "Holiday added", "calendar": HOLIDAY_CALENDAR}), 201
    return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
