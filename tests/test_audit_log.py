import importlib

def test_import_audit_log():
    module = importlib.import_module("audit_log")
    assert module is not None