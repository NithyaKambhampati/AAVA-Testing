import importlib

def test_import_responsive_ui():
    module = importlib.import_module("responsive_ui")
    assert module is not None