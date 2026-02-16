import importlib

def test_import_demo1():
    module = importlib.import_module("demo1")
    assert module is not None