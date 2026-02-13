import importlib

def test_import_approve_reject_leave():
    module = importlib.import_module("approve_reject_leave")
    assert module is not None