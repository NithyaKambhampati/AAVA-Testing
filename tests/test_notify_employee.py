import importlib

def test_import_notify_employee():
    module = importlib.import_module("notify_employee")
    assert module is not None