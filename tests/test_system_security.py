import importlib

def test_import_system_security():
    module = importlib.import_module("system_security")
    assert module is not None