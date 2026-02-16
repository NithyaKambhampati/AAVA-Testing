import importlib

def test_import_hr_admin_leave_reporting():
    module = importlib.import_module("hr_admin_leave_reporting")
    assert module is not None