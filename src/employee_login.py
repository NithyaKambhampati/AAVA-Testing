import ldap

class EmployeeLogin:
    def __init__(self, ldap_server, base_dn):
        self.ldap_server = ldap_server
        self.base_dn = base_dn

    def authenticate(self, username, password):
        try:
            conn = ldap.initialize(self.ldap_server)
            user_dn = f"uid={username},{self.base_dn}"
            conn.simple_bind_s(user_dn, password)
            return True, "Authentication successful"
        except ldap.INVALID_CREDENTIALS:
            return False, "Invalid credentials"
        except ldap.LDAPError as e:
            return False, f"LDAP error: {str(e)}"
        finally:
            try:
                conn.unbind_s()
            except:
                pass

if __name__ == "__main__":
    ldap_server = "ldap://your-org-ldap-server"
    base_dn = "ou=employees,dc=yourorg,dc=com"
    username = input("Enter username: ")
    password = input("Enter password: ")
    login = EmployeeLogin(ldap_server, base_dn)
    success, message = login.authenticate(username, password)
    print(message)