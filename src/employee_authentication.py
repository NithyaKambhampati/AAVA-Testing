# Employee Authentication and Role-Based Access
# Implements login, credential validation, and role-based feature exposure

class User:
 def __init__(self, username, password, role):
 self.username = username
 self.password = password
 self.role = role

class Authenticator:
 def __init__(self, user_db):
 self.user_db = user_db # user_db is a dict: username -> (password, role)

 def login(self, username, password):
 if username not in self.user_db:
 return {'success': False, 'error': 'Invalid credentials'}
 stored_password, role = self.user_db[username]
 if password != stored_password:
 return {'success': False, 'error': 'Invalid credentials'}
 return {'success': True, 'role': role}

 def get_features_for_role(self, role):
 features = {
 'employee': ['view_details', 'apply_leave', 'view_history', 'modify_request'],
 'manager': ['approve_leave', 'view_team_requests'],
 'hr_admin': ['configure_leave', 'view_reports', 'manage_users']
 }
 return features.get(role, [])

# Example usage:
user_db = {
 'alice': ('password123', 'employee'),
 'bob': ('managerpass', 'manager'),
 'carol': ('adminpass', 'hr_admin')
}
auth = Authenticator(user_db)
result = auth.login('alice', 'password123')
if result['success']:
 print(f"Logged in as {result['role']}")
 print("Features:", auth.get_features_for_role(result['role']))
else:
 print(result['error'])
