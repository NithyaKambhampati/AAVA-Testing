import importlib

def test_import_secure_login():
    module = importlib.import_module("secure_login")
    assert module is not None