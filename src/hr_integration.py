import requests
import sqlite3
from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key'
DATABASE = 'lms.db'
HR_API_ENDPOINT = 'https://hr.example.com/api/employees'

@app.route('/sync-hr')
def sync_hr():
    if 'username' not in session or session.get('role') not in ['admin', 'hr']:
        return redirect(url_for('login'))
    try:
        response = requests.get(HR_API_ENDPOINT, timeout=10)
        response.raise_for_status()
        employees = response.json()
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        for emp in employees:
            cur.execute("REPLACE INTO users (username, name, email, role, manager_id, status) VALUES (?, ?, ?, ?, ?, ?)",
                        (emp['username'], emp['name'], emp['email'], emp['role'], emp['manager_id'], emp['status']))
        conn.commit()
        conn.close()
        return 'HR data synchronized successfully.'
    except Exception as e:
        return f'Error syncing with HR system: {e}'

if __name__ == '__main__':
    app.run(debug=True)