import importlib

def test_import_audit_trail():
    module = importlib.import_module("audit_trail")
    assert module is not None