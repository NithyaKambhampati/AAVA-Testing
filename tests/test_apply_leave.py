import pytest

from src import app
 
 
def test_apply_leave_returns_value():

    result = app.apply_leave(None, None, None, None, None)

    assert result is not None

