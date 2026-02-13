import importlib

def test_import_usability_accessibility():
    module = importlib.import_module("usability_accessibility")
    assert module is not None