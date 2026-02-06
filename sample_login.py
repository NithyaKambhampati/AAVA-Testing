import hashlib

USERS_DB = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest()
}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login(username: str, password: str) -> bool:
    return USERS_DB.get(username) == hash_password(password)
