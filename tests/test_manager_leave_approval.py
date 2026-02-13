import importlib

def test_import_manager_leave_approval():
    module = importlib.import_module("manager_leave_approval")
    assert module is not None