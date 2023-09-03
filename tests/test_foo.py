from src.foo import add


def test_add_int():
    assert add(1, 2) == 3


def test_add_str():
    assert add("foo", "bar") == "foo bar"


def test_add_int_str():
    assert add(1, "bar") == None
