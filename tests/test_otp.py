import importlib

def test_import_otp():
    module = importlib.import_module("otp")
    assert module is not None
