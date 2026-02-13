import importlib

def test_import_hr_admin_access():
    module = importlib.import_module("hr_admin_access")
    assert module is not None