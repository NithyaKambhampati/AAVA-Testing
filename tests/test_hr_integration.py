import importlib

def test_import_hr_integration():
    module = importlib.import_module("hr_integration")
    assert module is not None