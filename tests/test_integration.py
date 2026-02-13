import importlib

def test_import_integration():
    module = importlib.import_module("integration")
    assert module is not None