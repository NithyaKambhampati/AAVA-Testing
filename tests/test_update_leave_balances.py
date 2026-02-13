import importlib

def test_import_update_leave_balances():
    module = importlib.import_module("update_leave_balances")
    assert module is not None