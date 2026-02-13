import importlib

def test_import_validate_leave_requests():
    module = importlib.import_module("validate_leave_requests")
    assert module is not None