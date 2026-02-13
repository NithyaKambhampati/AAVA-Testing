from flask import Flask, session, redirect, url_for, render_template, request
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'
DATABASE = 'lms.db'

@app.route('/admin/config', methods=['GET', 'POST'])
def admin_config():
    if 'username' not in session or session.get('role') not in ['hr', 'admin']:
        return redirect(url_for('login'))
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    if request.method == 'POST':
        config_type = request.form['config_type']
        if config_type == 'leave_type':
            name = request.form['name']
            accrual_rule = request.form['accrual_rule']
            cur.execute("INSERT INTO leave_types (name, accrual_rule) VALUES (?, ?)", (name, accrual_rule))
        elif config_type == 'holiday':
            date = request.form['date']
            desc = request.form['description']
            cur.execute("INSERT INTO holidays (date, description) VALUES (?, ?)", (date, desc))
        conn.commit()
    cur.execute("SELECT name, accrual_rule FROM leave_types")
    leave_types = cur.fetchall()
    cur.execute("SELECT date, description FROM holidays")
    holidays = cur.fetchall()
    conn.close()
    return render_template('admin_config.html', leave_types=leave_types, holidays=holidays)

if __name__ == '__main__':
    app.run(debug=True)