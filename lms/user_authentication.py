"""
User Authentication and Role-Based Access
Implements login with organizational credentials and role-based feature access.
"""

from enum import Enum

class Role(Enum):
 EMPLOYEE = 'employee'
 MANAGER = 'manager'
 HR = 'hr'
 ADMIN = 'admin'

class User:
 def __init__(self, username, role):
 self.username = username
 self.role = Role(role)
 self.is_authenticated = False

 def authenticate(self, credentials):
 # Placeholder for actual authentication (SSO/LDAP)
 if credentials.get('valid'):
 self.is_authenticated = True
 return True
 return False

 def has_access(self, feature):
 # Map features to roles for RBAC
 feature_roles = {
 'view_dashboard': [Role.EMPLOYEE, Role.MANAGER, Role.HR, Role.ADMIN],
 'approve_leave': [Role.MANAGER],
 'configure_policy': [Role.HR, Role.ADMIN],
 }
 return self.role in feature_roles.get(feature, [])

# Example usage:
# user = User('john.doe', 'employee')
# if user.authenticate({'valid': True}):
# print(user.has_access('view_dashboard'))
