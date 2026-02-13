import importlib

def test_import_audit_trail_logging():
    module = importlib.import_module("audit_trail_logging")
    assert module is not None