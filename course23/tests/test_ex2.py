# -*- coding: utf-8 -*-


def test_upper():
    assert 'foo'.upper() == 'FOO'

    assert 'foo'.upper() != 'FOO'
    # assert 'foo'.upper() in 'FOO'
    # assert 'foo'.upper() not in 'FOO'
