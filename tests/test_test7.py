import importlib

def test_import_test7():
    module = importlib.import_module("test7")
    assert module is not None