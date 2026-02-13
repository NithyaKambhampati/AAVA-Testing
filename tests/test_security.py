import importlib

def test_import_security():
    module = importlib.import_module("security")
    assert module is not None