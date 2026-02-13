import ldap
from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your-secret-key'

LDAP_SERVER = 'ldap://your-organization-ldap-server'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            ldap_conn = ldap.initialize(LDAP_SERVER)
            ldap_conn.simple_bind_s(f"uid={username},ou=users,dc=yourorg,dc=com", password)
            session['username'] = username
            return redirect(url_for('dashboard'))
        except ldap.INVALID_CREDENTIALS:
            return render_template('login.html', error='Invalid credentials. Access denied.')
        except ldap.LDAPError as e:
            return render_template('login.html', error='Authentication error. Please try again.')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return f"Welcome {session['username']} to LMS dashboard!"

if __name__ == '__main__':
    app.run(debug=True)