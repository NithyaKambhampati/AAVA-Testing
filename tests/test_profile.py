import importlib

def test_import_profile():
    module = importlib.import_module("profile")
    assert module is not None