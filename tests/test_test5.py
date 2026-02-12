import importlib

def test_import_test5():
    module = importlib.import_module("test5")
    assert module is not None
