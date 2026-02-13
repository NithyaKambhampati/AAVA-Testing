import importlib

def test_import_view_leave_balances():
    module = importlib.import_module("view_leave_balances")
    assert module is not None