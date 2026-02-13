import importlib

def test_import_authentication():
    module = importlib.import_module("authentication")
    assert module is not None