import importlib

def test_import_leave_workflow():
    module = importlib.import_module("leave_workflow")
    assert module is not None