from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your-secret-key'

ROLE_FEATURES = {
    'employee': ['dashboard', 'apply_leave', 'my_leaves'],
    'manager': ['dashboard', 'manager_requests'],
    'hr': ['dashboard', 'admin_config', 'admin_reports', 'audit_logs'],
    'admin': ['dashboard', 'admin_config', 'admin_reports', 'audit_logs'],
}

def has_access(feature):
    role = session.get('role')
    return feature in ROLE_FEATURES.get(role, [])

@app.before_request
def restrict_access():
    endpoint = request.endpoint
    if endpoint and not has_access(endpoint):
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)