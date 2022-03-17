#!/usr/bin/env python3

def inc(x):
    return x + 1


def test_inc():
    assert inc(3) == 4

def test_fail():
    assert inc(3) == 5
