import importlib

def test_import_manager_dashboard():
    module = importlib.import_module("manager_dashboard")
    assert module is not None