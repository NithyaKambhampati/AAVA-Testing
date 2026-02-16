import importlib

def test_import_data_security():
    module = importlib.import_module("data_security")
    assert module is not None