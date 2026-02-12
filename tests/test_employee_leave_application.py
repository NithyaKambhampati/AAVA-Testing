import importlib

def test_import_employee_leave_application():
    module = importlib.import_module("employee_leave_application")
    assert module is not None