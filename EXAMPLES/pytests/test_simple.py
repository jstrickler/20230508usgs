import pytest

def test_two_plus_two_equals_four():  # tests should begin with "test" (or will not be found automatically)
    assert 2 + 2 == 4   # if assert statement succeeds, the test passes
    assert 3 + 3 == 6


def test_zen():
    # create instance of component or call function
    # assert result is expected
    assert True

def test_floats():
    print(.1 + .2, end=" ")
    assert (.1 + .2) == pytest.approx(.3)

