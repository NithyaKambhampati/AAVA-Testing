import importlib

def test_import_leave_request_approval_workflow():
    module = importlib.import_module("leave_request_approval_workflow")
    assert module is not None