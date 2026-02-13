from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def home():
    return render_template('index.html')

# Note: index.html should be a responsive HTML template with accessibility features
# Example snippet (to be placed in templates/index.html):
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LMS Home</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">LMS</a>
    </nav>
    <div class="container mt-4">
        <h1>Welcome to Leave Management System</h1>
        <p>Accessible from desktop and mobile devices.</p>
        <a href="/login" class="btn btn-primary">Login</a>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)