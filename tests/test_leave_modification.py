import importlib

def test_import_leave_modification():
    module = importlib.import_module("leave_modification")
    assert module is not None