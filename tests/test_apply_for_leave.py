import importlib

def test_import_apply_for_leave():
    module = importlib.import_module("apply_for_leave")
    assert module is not None