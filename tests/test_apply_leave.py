import importlib

def test_import_apply_leave():
    module = importlib.import_module("apply_leave")
    assert module is not None