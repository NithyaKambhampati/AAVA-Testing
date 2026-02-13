"""
User Authentication Module
- Allows users (employee, manager, HR) to log in with organizational credentials
- Handles invalid credential attempts
"""

from typing import Optional
import hashlib

# Simulated user database (for demo purposes)
USER_DB = {
    'alice@company.com': {'password': 'hashed_password_1', 'role': 'employee'},
    'bob@company.com': {'password': 'hashed_password_2', 'role': 'manager'},
    'carol@company.com': {'password': 'hashed_password_3', 'role': 'hr'}
}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(email: str, password: str) -> Optional[dict]:
    user = USER_DB.get(email)
    if not user:
        return None
    if user['password'] == hash_password(password):
        return {'email': email, 'role': user['role']}
    return None

if __name__ == "__main__":
    # Example usage
    email = input("Email: ")
    password = input("Password: ")
    user_info = authenticate_user(email, password)
    if user_info:
        print(f"Login successful! Role: {user_info['role']}")
    else:
        print("Invalid credentials. Access denied.")
