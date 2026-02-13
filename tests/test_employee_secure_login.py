import importlib

def test_import_employee_secure_login():
    module = importlib.import_module("employee_secure_login")
    assert module is not None