import importlib

def test_import_hr_system_integration():
    module = importlib.import_module("hr_system_integration")
    assert module is not None