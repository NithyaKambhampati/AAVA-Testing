import importlib

def test_import_integration_hr_systems():
    module = importlib.import_module("integration_hr_systems")
    assert module is not None