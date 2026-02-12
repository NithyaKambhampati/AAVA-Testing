import importlib

def test_import_email():
    module = importlib.import_module("email")
    assert module is not None
