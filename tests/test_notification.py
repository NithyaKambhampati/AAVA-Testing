import importlib

def test_import_notification():
    module = importlib.import_module("notification")
    assert module is not None