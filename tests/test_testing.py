import importlib

def test_import_testing():
    module = importlib.import_module("testing")
    assert module is not None