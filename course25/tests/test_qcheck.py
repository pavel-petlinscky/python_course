# -*- coding: utf-8 -*-
import pytest
from pytest import list_of

# https://pypi.python.org/pypi/pytest-quickcheck


@pytest.mark.randomize(l=list_of(int), ncalls=100)
def test_sorting(l):
    sorted_l = sorted(l)
    assert all(sorted_l[i] <= sorted_l[i+1] for i in range(len(sorted_l)-1))


@pytest.mark.randomize(xs=list_of(int), ncalls=100)
def test_sorting(xs):
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys
