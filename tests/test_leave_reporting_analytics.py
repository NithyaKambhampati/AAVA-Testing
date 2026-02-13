import importlib

def test_import_leave_reporting_analytics():
    module = importlib.import_module("leave_reporting_analytics")
    assert module is not None