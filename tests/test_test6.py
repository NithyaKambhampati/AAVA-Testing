import importlib

def test_import_test6():
    module = importlib.import_module("test6")
    assert module is not None