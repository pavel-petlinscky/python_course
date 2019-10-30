from hypothesis import given
import hypothesis.strategies as st
from hypothesis import settings

# https://github.com/HypothesisWorks/hypothesis-python


@given(st.integers(), st.integers())
@settings(max_examples=1000)
def test_ints_are_commutative(x, y):
    assert x + y == y + x


@given(x=st.integers(), y=st.integers())
@settings(max_examples=1000)
def test_ints_cancel(x, y):
    assert (x + y) - y == x


@given(st.lists(st.integers()))
@settings(max_examples=1000)
def test_reversing_twice_gives_same_list(xs):
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys


@given(st.lists(st.integers()))
@settings(max_examples=1000)
def test_sorting(l):
    sorted_l = sorted(l)
    assert all(sorted_l[i] <= sorted_l[i+1] for i in range(len(sorted_l)-1))


@given(st.tuples(st.booleans(), st.text()))
@settings(max_examples=1000)
def test_look_tuples_work_too(t):
    # A tuple is generated as the one you provided, with the corresponding
    # types in those positions.
    assert len(t) == 2
    assert isinstance(t[0], bool)
    assert isinstance(t[1], str)
