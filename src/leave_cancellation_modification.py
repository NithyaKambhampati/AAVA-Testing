from flask import Flask, session, redirect, url_for, render_template, request
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'
DATABASE = 'lms.db'

@app.route('/my-leaves', methods=['GET', 'POST'])
def my_leaves():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    if request.method == 'POST':
        leave_id = request.form['leave_id']
        action = request.form['action']
        if action == 'cancel':
            cur.execute("SELECT status FROM leaves WHERE id=? AND username=?", (leave_id, session['username']))
            status = cur.fetchone()
            if status and status[0] == 'pending':
                cur.execute("UPDATE leaves SET status='cancelled' WHERE id=?", (leave_id,))
        elif action == 'modify':
            new_start = request.form['start_date']
            new_end = request.form['end_date']
            cur.execute("SELECT status FROM leaves WHERE id=? AND username=?", (leave_id, session['username']))
            status = cur.fetchone()
            if status and status[0] == 'pending':
                cur.execute("UPDATE leaves SET start_date=?, end_date=?, status='pending' WHERE id=?", (new_start, new_end, leave_id))
        conn.commit()
    cur.execute("SELECT id, leave_type, start_date, end_date, status FROM leaves WHERE username=? ORDER BY start_date DESC", (session['username'],))
    leaves = cur.fetchall()
    conn.close()
    return render_template('my_leaves.html', leaves=leaves)

if __name__ == '__main__':
    app.run(debug=True)