from flask import Flask, session, redirect, url_for, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'
DATABASE = 'lms.db'

def log_action(action, entity, entity_id, user_id, details):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    timestamp = datetime.now().isoformat()
    cur.execute("INSERT INTO audit_logs (action, entity, entity_id, user_id, details, timestamp) VALUES (?, ?, ?, ?, ?, ?)", (action, entity, entity_id, user_id, details, timestamp))
    conn.commit()
    conn.close()

@app.route('/admin/audit', methods=['GET'])
def audit_logs():
    if 'username' not in session or session.get('role') not in ['hr', 'admin']:
        return redirect(url_for('login'))
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT action, entity, entity_id, user_id, details, timestamp FROM audit_logs ORDER BY timestamp DESC")
    logs = cur.fetchall()
    conn.close()
    return render_template('audit_logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)