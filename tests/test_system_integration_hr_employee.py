import importlib

def test_import_system_integration_hr_employee():
    module = importlib.import_module("system_integration_hr_employee")
    assert module is not None