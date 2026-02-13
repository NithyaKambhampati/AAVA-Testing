import importlib

def test_import_sample_login():
    module = importlib.import_module("sample_login")
    assert module is not None