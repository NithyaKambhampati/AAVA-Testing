import importlib

def test_import_data_security_access_control():
    module = importlib.import_module("data_security_access_control")
    assert module is not None