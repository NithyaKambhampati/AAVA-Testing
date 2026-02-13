from flask import Flask, request, session, redirect, url_for, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'
DATABASE = 'lms.db'

@app.route('/apply-leave', methods=['GET', 'POST'])
def apply_leave():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        leave_type = request.form['leave_type']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        reason = request.form.get('reason', '')
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        # Validate balance
        cur.execute("SELECT leave_balance FROM users WHERE username=? AND leave_type=?", (session['username'], leave_type))
        balance = cur.fetchone()
        if not balance or balance[0] <= 0:
            conn.close()
            return render_template('apply_leave.html', error='Insufficient leave balance.')
        # Validate dates
        cur.execute("SELECT start_date, end_date FROM leaves WHERE username=? AND status='approved'", (session['username'],))
        for row in cur.fetchall():
            if (start_date <= row[1] and end_date >= row[0]):
                conn.close()
                return render_template('apply_leave.html', error='Overlapping leave dates.')
        # Insert leave request
        cur.execute("INSERT INTO leaves (username, leave_type, start_date, end_date, reason, status) VALUES (?, ?, ?, ?, ?, 'pending')", (session['username'], leave_type, start_date, end_date, reason))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('apply_leave.html')

if __name__ == '__main__':
    app.run(debug=True)