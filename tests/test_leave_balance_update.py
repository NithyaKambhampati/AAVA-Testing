import importlib

def test_import_leave_balance_update():
    module = importlib.import_module("leave_balance_update")
    assert module is not None