from flask import Flask, session, redirect, url_for, render_template, request
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'
DATABASE = 'lms.db'

@app.route('/manager/requests', methods=['GET', 'POST'])
def manager_requests():
    if 'username' not in session or session.get('role') != 'manager':
        return redirect(url_for('login'))
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT id, username, leave_type, start_date, end_date, reason, status FROM leaves WHERE manager=? AND status='pending'", (session['username'],))
    requests = cur.fetchall()
    if request.method == 'POST':
        leave_id = request.form['leave_id']
        action = request.form['action']
        comment = request.form.get('comment', '')
        if action == 'approve':
            cur.execute("UPDATE leaves SET status='approved', manager_comment=? WHERE id=?", (comment, leave_id))
            # Update leave balance
            cur.execute("SELECT username, leave_type, start_date, end_date FROM leaves WHERE id=?", (leave_id,))
            row = cur.fetchone()
            if row:
                username, leave_type, start_date, end_date = row
                days = (datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days + 1
                cur.execute("UPDATE users SET leave_balance = leave_balance - ? WHERE username=? AND leave_type=?", (days, username, leave_type))
        elif action == 'reject':
            cur.execute("UPDATE leaves SET status='rejected', manager_comment=? WHERE id=?", (comment, leave_id))
        conn.commit()
    conn.close()
    return render_template('manager_requests.html', requests=requests)

if __name__ == '__main__':
    app.run(debug=True)