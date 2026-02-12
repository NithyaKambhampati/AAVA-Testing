import importlib

def test_import_agent_testing():
    module = importlib.import_module("agent_testing")
    assert module is not None
