import importlib

def test_import_myToolTest():
    module = importlib.import_module("myToolTest")
    assert module is not None