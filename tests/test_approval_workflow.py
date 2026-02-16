import importlib

def test_import_approval_workflow():
    module = importlib.import_module("approval_workflow")
    assert module is not None