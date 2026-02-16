import importlib

def test_import_reporting():
    module = importlib.import_module("reporting")
    assert module is not None