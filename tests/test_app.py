import pytest
from src import app

def test_notify_on_comment_returns_value():
    result = app.notify_on_comment(None, None)
    assert result is not None
