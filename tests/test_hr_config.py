import importlib

def test_import_hr_config():
    module = importlib.import_module("hr_config")
    assert module is not None