import importlib

def test_import_manager():
    module = importlib.import_module("manager")
    assert module is not None