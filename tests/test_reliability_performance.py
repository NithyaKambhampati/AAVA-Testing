import importlib

def test_import_reliability_performance():
    module = importlib.import_module("reliability_performance")
    assert module is not None