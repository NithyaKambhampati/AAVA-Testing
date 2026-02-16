import importlib

def test_import_hr_admin_config():
    module = importlib.import_module("hr_admin_config")
    assert module is not None