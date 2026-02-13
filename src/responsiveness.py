"""
System Responsiveness and Mobile/Desktop Accessibility
As a user, I want the LMS to be easy to use and accessible on both desktop and mobile devices so that I can manage leave anywhere, anytime.
"""

# This is a backend placeholder; frontend should use responsive web frameworks (e.g., React, Bootstrap).
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "message": "LMS backend responsive and healthy."}), 200

if __name__ == '__main__':
    app.run(debug=True)
