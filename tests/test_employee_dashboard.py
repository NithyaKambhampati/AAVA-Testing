import importlib

def test_import_employee_dashboard():
    module = importlib.import_module("employee_dashboard")
    assert module is not None