import importlib

def test_import_role_based_access_control():
    module = importlib.import_module("role_based_access_control")
    assert module is not None