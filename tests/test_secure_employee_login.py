import importlib

def test_import_secure_employee_login():
    module = importlib.import_module("secure_employee_login")
    assert module is not None