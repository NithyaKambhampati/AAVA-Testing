import importlib

def test_import_ui():
    module = importlib.import_module("ui")
    assert module is not None