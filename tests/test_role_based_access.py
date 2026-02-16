import importlib

def test_import_role_based_access():
    module = importlib.import_module("role_based_access")
    assert module is not None