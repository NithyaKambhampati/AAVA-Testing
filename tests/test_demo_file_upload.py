import importlib

def test_import_demo_file_upload():
    module = importlib.import_module("demo_file_upload")
    assert module is not None
