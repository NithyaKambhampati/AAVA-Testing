import importlib

def test_import_hr_admin_reports():
    module = importlib.import_module("hr_admin_reports")
    assert module is not None