import importlib

def test_import_view_personal_leave_details():
    module = importlib.import_module("view_personal_leave_details")
    assert module is not None