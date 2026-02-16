import importlib

def test_import_demo():
    module = importlib.import_module("demo")
    assert module is not None