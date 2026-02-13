"""
Employee Authentication and Access
As an employee, I want to authenticate using my organizational credentials, so that I can securely access my leave dashboard.
"""
import hashlib

class AuthService:
    def __init__(self, user_db):
        self.user_db = user_db

    def authenticate(self, username, password):
        user = self.user_db.get(username)
        if user and user['password_hash'] == hashlib.sha256(password.encode()).hexdigest():
            return {'status': 'success', 'dashboard': user['dashboard']}
        return {'status': 'error', 'message': 'Invalid credentials'}

# Example user_db
user_db = {
    'john.doe': {'password_hash': hashlib.sha256(b'secret123').hexdigest(), 'dashboard': {'leaves': [], 'balance': 10}},
}

auth_service = AuthService(user_db)

if __name__ == '__main__':
    # Simulate login
    username = input('Username: ')
    password = input('Password: ')
    result = auth_service.authenticate(username, password)
    print(result)
