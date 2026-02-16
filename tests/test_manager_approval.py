import importlib

def test_import_manager_approval():
    module = importlib.import_module("manager_approval")
    assert module is not None