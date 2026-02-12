import importlib

def test_import_view_personal_leave():
    module = importlib.import_module("view_personal_leave")
    assert module is not None