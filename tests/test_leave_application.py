import importlib

def test_import_leave_application():
    module = importlib.import_module("leave_application")
    assert module is not None