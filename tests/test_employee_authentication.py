import importlib

def test_import_employee_authentication():
    module = importlib.import_module("employee_authentication")
    assert module is not None