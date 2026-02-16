import importlib

def test_import_hr_admin_leave_policy_configuration():
    module = importlib.import_module("hr_admin_leave_policy_configuration")
    assert module is not None