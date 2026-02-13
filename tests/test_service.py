import importlib

def test_import_service():
    module = importlib.import_module("service")
    assert module is not None