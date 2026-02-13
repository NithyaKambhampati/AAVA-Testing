import importlib

def test_import_view_personal_details():
    module = importlib.import_module("view_personal_details")
    assert module is not None