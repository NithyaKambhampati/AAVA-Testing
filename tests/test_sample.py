import importlib

def test_import_sample():
    module = importlib.import_module("sample")
    assert module is not None