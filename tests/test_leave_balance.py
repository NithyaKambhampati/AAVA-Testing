import importlib

def test_import_leave_balance():
    module = importlib.import_module("leave_balance")
    assert module is not None