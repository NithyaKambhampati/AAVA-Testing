import importlib

def test_import_employee_leave_dashboard():
    module = importlib.import_module("employee_leave_dashboard")
    assert module is not None