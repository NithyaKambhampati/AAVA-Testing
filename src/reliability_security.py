from flask import Flask, session, redirect, url_for, render_template
import logging
import ssl

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Setup logging
logging.basicConfig(filename='lms.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@app.before_request
def log_request():
    logging.info(f"User: {session.get('username', 'anonymous')} accessed {url_for('home')}")

@app.after_request
def set_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # For production, run behind HTTPS
    # context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # context.load_cert_chain('cert.pem', 'key.pem')
    # app.run(ssl_context=context)
    app.run(debug=True)