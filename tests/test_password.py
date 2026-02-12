import importlib

def test_import_password():
    module = importlib.import_module("password")
    assert module is not None