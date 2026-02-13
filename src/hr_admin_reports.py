from flask import Flask, session, redirect, url_for, render_template, request
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'
DATABASE = 'lms.db'

@app.route('/admin/reports', methods=['GET'])
def admin_reports():
    if 'username' not in session or session.get('role') not in ['hr', 'admin']:
        return redirect(url_for('login'))
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    team = request.args.get('team')
    if team:
        cur.execute("SELECT username, leave_type, start_date, end_date, status FROM leaves WHERE team=?", (team,))
        report = cur.fetchall()
    else:
        cur.execute("SELECT username, leave_type, start_date, end_date, status FROM leaves")
        report = cur.fetchall()
    conn.close()
    return render_template('admin_reports.html', report=report)

if __name__ == '__main__':
    app.run(debug=True)