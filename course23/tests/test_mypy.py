def foo(x: int) -> int:
    return x * 2


def bar(x: int) -> str:
    return x * 2


def baz(x: int) -> int:
    return str(x) * 2


def test_foo():
    assert foo(12) == 24


def test_bar():
    assert bar(12) == 24


def test_baz():
    assert baz(12) == "1212"


def test_qux():
    assert foo("12") == "1212"
