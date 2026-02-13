import importlib

def test_import_hr_reporting():
    module = importlib.import_module("hr_reporting")
    assert module is not None