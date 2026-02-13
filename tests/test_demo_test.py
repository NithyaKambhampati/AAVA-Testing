import importlib

def test_import_demo_test():
    module = importlib.import_module("demo_test")
    assert module is not None