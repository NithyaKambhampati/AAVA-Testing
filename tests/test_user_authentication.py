import importlib

def test_import_user_authentication():
    module = importlib.import_module("user_authentication")
    assert module is not None