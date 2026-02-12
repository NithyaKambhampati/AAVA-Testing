import importlib

def test_import_query():
    module = importlib.import_module("query")
    assert module is not None