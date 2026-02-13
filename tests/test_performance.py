import importlib

def test_import_performance():
    module = importlib.import_module("performance")
    assert module is not None