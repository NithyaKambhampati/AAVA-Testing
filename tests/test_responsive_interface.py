import importlib

def test_import_responsive_interface():
    module = importlib.import_module("responsive_interface")
    assert module is not None