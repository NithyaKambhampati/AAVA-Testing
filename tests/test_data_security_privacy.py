import importlib

def test_import_data_security_privacy():
    module = importlib.import_module("data_security_privacy")
    assert module is not None