import importlib

def test_import_login():
    module = importlib.import_module("login")
    assert module is not None
